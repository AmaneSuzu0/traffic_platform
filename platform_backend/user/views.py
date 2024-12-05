from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework_jwt.settings import api_settings
from user.models import SysUser, SysUserSerializer


class TestView(View):
    """测试接口，需要前端带上token"""

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')  # 尝试去获取token
        print("token:", token)
        if token is not None and token != '':  # 如果有token，则验证token
            userList_obj = SysUser.objects.all()
            print(userList_obj, type(userList_obj))  # 打印结果会发现格式不是Json格式，而是QuerySet类型，需要转换
            userlist = list(userList_obj.values())  # 转换为列表
            return JsonResponse({'code': 200, 'message': 'test!', 'data': userlist})
        else:
            return JsonResponse({'code': 401, 'message': 'token is required!'})


class JwtTestView(View):
    """jwt测试接口,生成token返回给前端"""

    def get(self, request):
        user = SysUser.objects.get(username='admin', password='123456')
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 用来把user对象转换为载荷的函数
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 用来编码生成token的函数
        payload = jwt_payload_handler(user)  # 生成载荷
        token = jwt_encode_handler(payload)  # 生成token
        # token返回给前端，前端可以把token存储到localStorage中，每次请求都带上token
        return JsonResponse({'code': 200, 'token': token})


class LoginView(View):
    """用户登陆逻辑实现"""

    def post(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            user = SysUser.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 用来把user对象转换为载荷的函数
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 用来编码生成token的函数
            payload = jwt_payload_handler(user)  # 生成载荷
            token = jwt_encode_handler(payload)  # 生成token
        except Exception as e:  # 未能获取到用户信息
            print(e)
            return JsonResponse({'code': 500, 'message': '用户名或密码错误！'})
        # 若能查询到用户信息，则使用把user对象转换为json格式的序列化器，并返回给前端，同时返回token
        return JsonResponse({'code': 200, 'token': token, 'user': SysUserSerializer(user).data, 'message': '登陆成功！'})

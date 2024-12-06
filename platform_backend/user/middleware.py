from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from jwt import ExpiredSignatureError, InvalidTokenError, PyJWTError
from rest_framework_jwt.settings import api_settings


class JwtAuthenticationMiddleware(MiddlewareMixin):
    """django中间件，用于验证token"""
    """在请求到达视图函数之前，先调用中间件，判断是否需要验证token"""
    def process_request(self, request):
        white_list = ["/user/login", "/user/register", "/user/logout"]  # 请求白名单,登陆注册登出不验证token
        path = request.path
        if path not in white_list and not path.startswith("/media"): # 白名单内的请求和媒体文件不验证token
            print("要进行token验证")
            # requst.META里面包含了请求头信息，包括HTTP_AUTHORIZATION(也就是token)
            token = request.META.get('HTTP_AUTHORIZATION')
            print("token:", token)
            try:
                jwt_decode_handler = api_settings.JWT_DECODE_HANDLER  # 获取jwt的解码函数
                jwt_decode_handler(token)  # 解码token，如果失败会抛出异常
            except ExpiredSignatureError:
                return HttpResponse('Token过期，请重新登录！')
            except InvalidTokenError:
                return HttpResponse('Token验证失败！')
            except PyJWTError:
                return HttpResponse('Token验证异常！')
        else:
            print("不验证验证")
            return None

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework_jwt.settings import api_settings
from typing import Set, List

from menu.models import SysMenu, SysMenuSerializer
from role.models import SysRole
from user.models import SysUser, SysUserSerializer


class LoginView(View):
    """用户登陆逻辑实现"""

    def buildTreeMenu(self, sysMenuList):
        # 递归函数，用于构建树形菜单
        resultMenuList: List[SysMenu] = list()
        for menu in sysMenuList:
            # 当前菜单
            for e in sysMenuList:  # 寻找子菜单
                if e.parent_id == menu.id:
                    if not hasattr(menu, 'children'):
                        menu.children = list()
                    menu.children.append(e)

            if menu.parent_id == 0:
                resultMenuList.append(menu)
        return resultMenuList

    def post(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            user = SysUser.objects.get(username=username, password=password)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 用来把user对象转换为载荷的函数
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 用来编码生成token的函数
            payload = jwt_payload_handler(user)  # 生成载荷
            token = jwt_encode_handler(payload)  # 生成token
            # 把该用户的导航栏信息返回给前端，前端根据该信息展示导航栏-------------
            roleList = SysRole.objects.raw(  # 该用户的角色列表
                # 先根据用户id查到其角色，得到角色的id和name
                "SELECT id, name FROM sys_role WHERE id IN (SELECT role_id FROM sys_user_role WHERE user_id=%s)",
                [user.id]
            )
            print("roleList=", roleList)
            menuSet: Set[SysMenu] = set()  # 该用户的菜单集合
            for role in roleList:  # 遍历该用户的角色列表
                print(role.id, role.name)
                menuList = SysMenu.objects.raw(  # 对于每个角色，查询其对应的菜单列表
                    "SELECT * FROM sys_menu WHERE id IN (SELECT menu_id FROM sys_role_menu WHERE role_id=%s)", [role.id]
                )
                for menu in menuList:
                    menuSet.add(menu)  # 将菜单加入到菜单集合中
            menuList: List[SysMenu] = list(menuSet)  # 将菜单集合转换为列表
            sortedMenuList = sorted(menuList)  # 排序
            sysMenuList: List[SysMenu] = self.buildTreeMenu(sortedMenuList)
            serializerMenuList = list()
            for sysMenu in sysMenuList:
                serializerMenuList.append(SysMenuSerializer(sysMenu).data)

        except Exception as e:  # 未能获取到用户信息
            print(e)
            return JsonResponse({'code': 500, 'message': '用户名或密码错误！'})
        # 若能查询到用户信息，则使用把user对象转换为json格式的序列化器，并返回给前端，同时返回token
        print("用户登录：", user.username)
        return JsonResponse({'code': 200, 'token': token, 'user': SysUserSerializer(user).data,
                             'message': '登陆成功！', 'menuList': serializerMenuList})

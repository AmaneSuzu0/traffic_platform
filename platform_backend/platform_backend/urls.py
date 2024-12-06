"""platform_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user/', include('user.urls')),  # 用户管理模块
    path('role/', include('role.urls')),  # 角色管理模块
    path('menu/', include('menu.urls')),  # 菜单管理模块

    # path('api/', include('api.urls')),  # 接口模块
    # path('data_prediction/', include('data_prediction.urls')),  # 流量数据预测模块
    # path('data_query/', include('data_query.urls')),  # 道路交通信息查询模块
    # path('map_display/', include('map_display.urls')),  # 地图展示模块
]

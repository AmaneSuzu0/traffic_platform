# 大数据交通平台(后端帮助文档)

## 1. 开发环境快速搭建

- **创建虚拟环境**

  利用conda创建一个新项目的虚拟环境。envname为新环境名称。

  ```shell
  conda create --name envname python=3.8
  ```

- 使用PyCharm打开platform_backend文件夹，并选择使用刚创建的新环境。

- **安装依赖库**

  ```shell
  pip install -r requirements.txt
  ```

- **创建数据库**

先创建一个数据库，然后在platform_backend/settings.py文件中修改DATABASES修改NAME、USER、PASSWORD（数据库名称、用户名、密码）

```shell
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME":  "db_traffic_platform",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

- **创建表**

```shell
python manage.py makemigrations
python manage.py migrate
```

- **导入sql数据**

先修改一键执行全部sql文件的init_all_sql.py文件

```python
# 数据库连接配置
config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'database_name',
}
```

修改完成后在终端执行，即可生成数据。

```shell
python init_all_sql.py
```

- **本地运行测试**


## 2. 项目概述

### 2.1项目背景

​	暂定

## 3. 技术栈

- **开发语言**：python
- **代码编辑器**：PyCharm
- **开发框架**：Django
- **包管理工具**：pip
- **数据库**：mysql
- **其他技术**：DRF、Jwt等

## 4.平台架构

### 4.1平台架构图

暂定

### 4.2模块划分

#### 4.2.1 platform_backend

主项目模块

#### 4.2.2 user

用户模块

- LoginView<=>/user/login：登陆视图。根据前端传来的账号密码信息查询用户数据表，将用户信息和生成的token返回前端。

#### 4.2.3 role

角色权限模块

#### 4.2.4 menu

菜单模块

#### 4.2.5 data_query

数据库数据查询模块

- GetNodesView<=>/data_query/get_nodes：获取交通节点信息视图。根据前端传来的区域信息查询交通节点表，将对应区域的节点信息返回前端。

#### 4.2.6 data_prediction

暂未使用

#### 4.2.7 map_display

暂未使用

#### 4.2.8 api

暂未使用

### 4.3数据表

#### 4.3.1 user模块

- 表名：sys_user
- 表实例：SysUser

```python
class SysUser(models.Model):
    """用户信息表"""
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    avatar = models.CharField(max_length=255, null=True, verbose_name="用户头像")
    email = models.CharField(max_length=100, null=True, verbose_name="用户邮箱")
    phonenumber = models.CharField(max_length=11, null=True, verbose_name="手机号码")
    login_date = models.DateField(null=True, verbose_name="最后登录时间")
    status = models.IntegerField(null=True, verbose_name="帐号状态（0正常 1停用）")
    create_time = models.DateField(null=True, verbose_name="创建时间", )
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=500, null=True, verbose_name="备注")

    class Meta:
        db_table = "sys_user"
```

#### 4.3.2 role模块

- 表名：sys_role
- 表实例：SysRole

```python
class SysRole(models.Model):
    """系统角色表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, verbose_name="角色名称")
    code = models.CharField(max_length=100, null=True, verbose_name="角色权限字符串")
    create_time = models.DateField(null=True, verbose_name="创建时间", )
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=500, null=True, verbose_name="备注")

    class Meta:
        db_table = "sys_role"
```

- 表名：sys_user_role
- 表实例：SysUserRole

```python
class SysUserRole(models.Model):
    """用户-角色关联表"""
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole, on_delete=models.PROTECT)
    user = models.ForeignKey(SysUser, on_delete=models.PROTECT)

    class Meta:
        db_table = "sys_user_role"
```

#### 4.3.3 menu模块

- 表名：sys_menu
- 表实例：SysMenu

```python
class SysMenu(models.Model):
    """系统菜单表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, verbose_name="菜单名称")
    icon = models.CharField(max_length=100, null=True, verbose_name="菜单图标")
    parent_id = models.IntegerField(null=True, verbose_name="父菜单ID")
    order_num = models.IntegerField(null=True, verbose_name="显示顺序")
    path = models.CharField(max_length=200, null=True, verbose_name="路由地址")
    component = models.CharField(max_length=255, null=True, verbose_name="组件路径")
    menu_type = models.CharField(max_length=1, null=True, verbose_name="菜单类型（M目录 C菜单 F按钮）")
    perms = models.CharField(max_length=100, null=True, verbose_name="权限标识")
    create_time = models.DateField(null=True, verbose_name="创建时间", )
    update_time = models.DateField(null=True, verbose_name="更新时间")
    remark = models.CharField(max_length=500, null=True, verbose_name="备注")

    # children = list()
    def __lt__(self, other):
        # 重写__lt__方法，使得菜单按照order_num排序
        return self.order_num < other.order_num

    class Meta:
        db_table = "sys_menu"
```

- 表名：sys_role_menu
- 表实例：SysRoleMenu

```python
class SysRoleMenu(models.Model):
    """系统角色菜单关联表"""
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(SysRole, on_delete=models.PROTECT)
    menu = models.ForeignKey(SysMenu, on_delete=models.PROTECT)

    class Meta:
        db_table = "sys_role_menu"
```

#### 4.3.4 data_query模块

- 表名：road_nodes
- 表实例：RoadNode

```python
class RoadNode(models.Model):
    """道路节点表"""
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=100, verbose_name="省份")
    city = models.CharField(max_length=100, verbose_name="城市")
    district = models.CharField(max_length=100, verbose_name="区县")
    node_name = models.CharField(max_length=255, verbose_name="道路节点名称")
    node_type = models.CharField(max_length=50, verbose_name="节点类型")
    longitude = models.FloatField(verbose_name="经度")
    latitude = models.FloatField(verbose_name="纬度")
    description = models.TextField(null=True, blank=True, verbose_name="描述信息")
    last_update_time = models.DateTimeField(auto_now=True, verbose_name="最近更新时间")

    class Meta:
        db_table = "road_nodes"
```

- 表名：traffic_history
- 表实例：TrafficHistory

```python
class TrafficHistory(models.Model):
    """历史流量表"""
    id = models.AutoField(primary_key=True)
    node = models.ForeignKey(RoadNode, on_delete=models.CASCADE, related_name="traffic_history", verbose_name="道路节点")
    date = models.DateField(verbose_name="日期")
    time_slot = models.CharField(max_length=50, verbose_name="时间段")
    traffic_value = models.IntegerField(verbose_name="流量值")
    weather_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="天气信息")
    special_events = models.CharField(max_length=255, null=True, blank=True, verbose_name="特殊事件")

    class Meta:
        db_table = "traffic_history"
```

- 表名：traffic_forecast
- 表实例：TrafficForecast

```python
class TrafficForecast(models.Model):
    """流量预测表"""
    id = models.AutoField(primary_key=True)
    node = models.ForeignKey(RoadNode, on_delete=models.CASCADE, related_name="traffic_forecast", verbose_name="道路节点")
    forecast_date = models.DateField(verbose_name="预测日期")
    time_slot = models.CharField(max_length=50, verbose_name="时间段")
    forecast_value = models.IntegerField(verbose_name="预测流量值")
    model_version = models.CharField(max_length=100, null=True, blank=True, verbose_name="模型版本")

    class Meta:
        db_table = "traffic_forecast"
```

#### 4.3.5 data_prediction模块

暂未使用

#### 4.3.6 map_display模块

暂未使用

#### 4.3.7 api模块

暂未使用

## 5. API

### 5.1 前后端通信规范

- get：处理前端获取数据请求

```python
def get(self, request):
```

- post：处理前端增添数据请求

```python
def post(self, request):
```

- put：处理前端更新数据请求

```python
def put(self, request):
```

- delete：处理前端删除数据请求

```python
def delete(self, request):
```

### 5.2 状态码约定

- **code=200**：请求成功
- **code=500**：请求失败，存在异常
- **code=404**：请求资源不存在或未找到



## 6. 说明文档版本

- 版本v1.0
  - 备注：起草后端帮助文档
  - 修改人员：陆通
  - 时间：2024年12月13日




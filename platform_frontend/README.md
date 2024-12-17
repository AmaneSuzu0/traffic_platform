# 大数据交通平台(前端帮助文档)

## 1. 开发环境快速搭建

- **安装依赖**

若依赖安装出现网络问题建议更换镜像。

```shell
npm install
```

```shell
npm install -g @vue/cli
npm install @vue/cli-service --save-dev
npm install element-china-area-data
```

- **本地运行**

```shell
npm run serve
```

- **编译打包**

```shell
npm run build
```

## 2. 项目概述
### 2.1项目背景

​	暂定

## 3. 技术栈

- **开发语言**：HTML, CSS, JavaScript

- **代码编辑器**：Visual Studio Code

- **开发框架**：Vue3

- **构建工具**：Webpack

- **包管理工具**：npm

- **其他技术**：Sass、axios、element-plus等

- **详情依赖查看package.json文件**：

  ```json
  "dependencies": {
      "axios": "^1.7.2",
      "core-js": "^3.8.3",
      "element-china-area-data": "^6.1.0",
      "element-plus": "^2.2.6",
      "js-cookie": "^3.0.1",
      "jsencrypt": "^3.2.1",
      "leaflet": "^1.9.4",
      "leaflet.markercluster": "^1.5.3",
      "qs": "^6.10.5",
      "sass": "^1.52.3",
      "sass-loader": "^13.0.0",
      "svg-sprite-loader": "^6.0.11",
      "vue": "^3.2.13",
      "vue-router": "^4.0.3",
      "vuex": "^4.0.0",
      "webpack": "^5.73.0"
    },
  ```

  

## 4.平台架构

### 4.1平台架构图

暂定

### 4.2文件划分

#### 4.2.1 assets

##### 4.2.1.1 images

仅用于存放 web界面所需要的静态图像，例如登陆界面的背景、学校logo、用户默认头像等等。

#####  4.2.1.2 styles

用于存放一些用于美化显示效果的.css文件。

#### 4.2.2 components

##### 4.2.2.1 SvgIcon

用来自定义Icon的组件。使用自定义icon的方式如下：

```html
<template #prefix><svg-icon icon="user" /></template>
<template #prefix><svg-icon icon="password" /></template>
```

#### 4.2.3 icons

用来存放各种各样的.svg文件。

#### 4.2.4 layout*

参考element布局容器方案，我们将整个页面的布局划分为footer、header、sidebar、main四个板块。

详情参考：https://element.eleme.cn/#/zh-CN/component/container

##### 4.2.4.1 footer

网页底部布局板块，仅用作展示版权声明文字。

##### 4.2.4.2 header

网页顶部布局板块，一般用作展示网站名称信息及用户头像。

- components：顶部布局需要的组件。例如Avatar.vue用作展示用户头像和个人信息安全退出等功能、HeaderLeft.vue用来展示平台logo和平台名称。
- Header.vue：使用了上面的components组件的顶部布局。

##### 4.2.4.3 sidebar

导航栏布局。实现从sessionstore里面获取当前用户所拥有的菜单信息列表。

菜单信息列表menuList中包含了一系列最外层父菜单，例如首页、交通数据库、交通流量地图等。每个最外层父菜单包含以下属性：

- **name**：菜单名称
- **icon**：菜单需要的图标
- **path**：点击该菜单按钮时需要跳转的路由
- **children**：子菜单元素

其中每个子菜单同样具有上述属性。

##### 4.2.4.4 main

与上述的三个布局不同的是，main文件夹中只用来存放内容布局(main)所需要用到的公共组件，而将内容布局真正需要展示的视图放入views中。

- AreaSelector.vue：地区选择器，用来选择xx省/xx市/xx区或县。

##### 4.2.4.5 index.vue*

```html
<template>
    <div class="app-wrapper">
        <el-container>
            <el-header>
                <Header></Header>
            </el-header>
            <el-container>
                <el-aside width="200px" class="sidebar-container">
                    <SideBar></SideBar>
                </el-aside>
                <el-container>
                    <el-main>
                        <router-view></router-view>
                    </el-main>
                    <el-footer>
                        <Footer></Footer>
                    </el-footer>
                </el-container>
            </el-container>
        </el-container>
    </div>
</template>
<script setup>
    import SideBar from '@/layout/sidebar/SideBar'
    import Header from '@/layout/header/Header'
    import Footer from '@/layout/footer/Footer'
</script>
```

可见我们将之前的Footer、Header、SideBar引入后，按照element的布局方案将这些组件使用。但是唯独在main的地方使用了：

```html
<el-main>
    <router-view></router-view>
</el-main>
```

在我们的前端项目中，我们采用了一个统一的布局结构，确保了每个页面都包含左侧导航栏（Sidebar）、顶部导航栏（Header）和底部说明栏（Footer）。为了实现这种统一布局，我们将这三个组件引入了主组件，并使用 Element UI 的布局方案。

在这个布局中，`<el-main>` 部分是重点，因它是页面内容的主要展示区域。我们使用 `<router-view>` 作为该部分的占位符，这样我们就可以根据路由的变化加载不同的子视图。换句话说，所有视图的主要结构是固定的，唯一变化的部分就是 `<router-view>` 中具体的内容。这样做的好处在于，我们不需要为每一个页面都重复编写 Header、Sidebar 和 Footer，提升了代码的可维护性和复用性。

#### 4.2.5 router

- **根路由配置**：配置的根路由是 `'/'`，它对应的组件是 `index`。当用户访问该路径时，会重定向到 `/index`，同时展示主页面的结构。
- **子路由设置**：在根路由下，我们定义了一系列子路由，所有这些子路由都共享同一个布局（Header、Sidebar、Footer），只有 `<router-view>` 中的内容会根据所导航的路径发生变化。每个子路由都与特定的组件关联，并有各自的路径和名称，例如：
  - `/index` 对应 `IndexView` 组件。
  - `/traffic_database/road_traffic` 对应 `RoadTrafficView` 组件。
  - `/traffic_map/road_map` 对应 `RoadMapView` 组件。
  - 以及其他几个与流量和管理相关的视图。
- **/user/login**：登陆界面视图路由(独立路由)
- **/index**：登陆后首页视图路由(/的子路由)
- **/traffic_database/road_traffic**：道路交通数据库视图路由(/的子路由)
- **/traffic_database/ship_traffic**：船运交通数据库视图路由(/的子路由)
- **/traffic_map/road_map**：道路交通流量地图视图路由(/的子路由)
- **/traffic_map/ship_map**：船运交通流量地图视图路由(/的子路由)
- **/admin_management/account_management**：管理员权限账户管理视图路由(/的子路由)
- **/admin_management/database_management**：管理员权限数据库管理视图路由(/的子路由)

#### 4.2.6 store

全局状态管理

#### 4.2.7 utils

- jsencrypt.js：实现对数据的加密和解密
- mapUtils.js：地图显示需要的工具
- request.js：封装axios的工具包

#### 4.2.8 views

- admin_management：管理员权限功能板块视图
- home：首页视图
- traffic_database：交通数据库视图
- traffic_map：交通流量地图视图
- user：用户相关视图

## 5. API

### 5.1 前后端通信规范

**关于封装好的request.js文件**

与后端通信统一采用已经封装好的request工具，使用方式如下：

- 在js代码中引入request工具

```javascript
import requestUtil from '@/utils/request'
```

- get：请求数据

  ```javascript
  //使用例子
  let result = await requestUtil.get('/data_query/get_nodes', {
                  province: province,
                  city: city,
                  district: district,
                  node_type: '船运交通',});
  ```

- post：提交数据数据

  ```javascript
  //使用例子
  let result = await requestUtil.post("user/login?" + qs.stringify(loginForm.value))
  ```

- del：删除请求

- fileUpload：上传文件(本质仍是post请求)

- getServerUrl：返回后端url

### 5.2 后端接口

- /user/login ：处理登陆请求，返回登陆用户信息。
- /data_query/get_nodes：处理交通节点信息请求，返回交通节点信息。

### 5.3 后端状态码约定

- **code=200**：请求成功
- **code=500**：请求失败，存在异常
- **code=404**：请求资源不存在或未找到

## 6. 说明文档版本

- 版本v1.0
  - 备注：起草前端帮助文档
  - 修改人员：陆通
  - 时间：2024年12月13日


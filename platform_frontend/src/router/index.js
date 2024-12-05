import { createRouter, createWebHashHistory } from 'vue-router'
import UserLoginView from '@/views/user/UserLoginView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: "/user/login/",
    meta: {
      requestAuth: true,
    }
  },

  {
    path: "/user/login/",
    name: "user_login",
    component: UserLoginView,
    meta: {
      requestAuth: false,  // 登陆界面，该路由不需要登录验证
    }
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

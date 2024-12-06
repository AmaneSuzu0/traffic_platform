import { createRouter, createWebHashHistory } from 'vue-router'
import UserLoginView from '@/views/user/UserLoginView.vue'
import IndexView from '@/views/home/IndexView.vue'
import RoadMapView from '@/views/traffic_map/RoadMapView.vue'
import RoadTrafficView from '@/views/traffic_database/RoadTrafficView.vue'
import ShipTrafficView from '@/views/traffic_database/ShipTrafficView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    redirect: "/user/login",
  },
  {
    path: '/index',
    name: 'index',
    component: IndexView,
  },

  {
    path: "/user/login",
    name: "user_login",
    component: UserLoginView,
  },
  {
    path: "/traffic_database/road_traffic",
    name: "traffic_database_road_traffic",
    component: RoadTrafficView,
  },
  {
    path: "/traffic_database/ship_traffic",
    name: "traffic_database_ship_traffic",
    component: ShipTrafficView,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

import { createRouter, createWebHistory } from 'vue-router'
import UserLoginView from '@/views/user/UserLoginView.vue'
import IndexView from '@/views/home/IndexView.vue'
import RoadMapView from '@/views/traffic_map/RoadMapView.vue'
import RoadTrafficView from '@/views/traffic_database/RoadTrafficView.vue'
import ShipTrafficView from '@/views/traffic_database/ShipTrafficView.vue'
import ShipMapView from '@/views/traffic_map/ShipMapView.vue'
import AccountManagementView from '@/views/admin_management/AccountManagementView.vue'
import DatabaseManagementView from '@/views/admin_management/DatabaseManagementView.vue'
import index from '@/layout/index.vue'



const routes = [
  {
    path: '/',
    name: 'home',
    component: index,
    redirect: '/index',
    children: [
      {
        path: '/index',
        name: 'index',
        component: IndexView,
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
      {
        path: "/traffic_map/road_map",
        name: "traffic_map_road_map",
        component: RoadMapView,
      },
      {
        path: "/traffic_map/ship_map",
        name: "traffic_map_ship_map",
        component: ShipMapView,
      },
      {
        path: "/admin_management/account_management",
        name: "admin_management_account_management",
        component: AccountManagementView,
      },
      {
        path: "/admin_management/database_management",
        name: "admin_management_database_management",
        component: DatabaseManagementView,
      },
    ]
  },
  {
    path: "/user/login",
    name: "user_login",
    component: UserLoginView,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

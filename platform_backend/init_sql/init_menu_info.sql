insert into
`sys_menu`(`id`,`name`,`icon`,`parent_id`,`order_num`,`path`,`component`,`menu_type`,`perms`,`create_time`,`update_time`,`remark`) values
(1,'交通数据库','table',0,1,'/traffic_database','','M','','2024-12-06','2024-12-06','交通数据库目录'),
(2,'交通流量地图','international',0,2,'/traffic_map','','M','','2024-12-06','2024-12-06','交通流量地图目录'),
(3,'管理员权限','system',0,3,'/admin_management','','M','','2024-12-06','2024-12-06','管理员权限目录'),
(4,'道路交通库','chart',1,1,'/traffic_database/road_traffic','traffic_database/RoadTrafficView','C','','2024-12-06','2024-12-06','道路交通数据库菜单'),
(5,'船运交通库','chart',1,2,'/traffic_database/ship_traffic','traffic_database/ShipTrafficView','C','','2024-12-06','2024-12-06','船运交通数据库菜单'),
(6,'道路交通地图','chart',2,1,'/traffic_map/road_map','traffic_map/RoadMapView','C','','2024-12-06','2024-12-06','道路交通流量地图菜单'),
(7,'船运交通地图','chart',2,2,'/traffic_map/ship_map','traffic_map/ShipMapView','C','','2024-12-06','2024-12-06','船运交通流量地图菜单'),
(8,'交通数据库管理','tree-table',3,1,'/admin_management/database_management','admin_management/DatabaseManagementView','C','system:database:list','2024-12-06','2024-12-06','交通数据库管理菜单'),
(9,'账户管理','peoples',3,2,'/admin_management/account_management','admin_management/AccountManagementView','C','system:user:list','2024-12-06','2024-12-06','账户管理菜单');

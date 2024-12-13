import mysql.connector

# 数据库连接配置
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'db_traffic_platform',
}

# 创建连接
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# 执行多个 SQL 文件
sql_files = [
    'init_sql/init_menu_info.sql',
    'init_sql/init_role_info.sql',
    'init_sql/init_sys_role_menu_info.sql',
    'init_sql/init_sys_user_role_info.sql',
    'init_sql/init_traffic_node_info.sql',
    'init_sql/init_user_info.sql',
]
for sql_file in sql_files:
    with open(sql_file, 'r') as file:
        sql_script = file.read()
        cursor.execute(sql_script)

# 提交更改并关闭连接
conn.commit()
cursor.close()
conn.close()

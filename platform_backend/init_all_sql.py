import mysql.connector

# 数据库连接配置
config = {
    'user': 'root',
    'password': 'naideli2233',
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
    'init_sql/init_user_info.sql',
    'init_sql/init_traffic_node_info.sql',
    'init_sql/init_sys_role_menu_info.sql',
    'init_sql/init_sys_user_role_info.sql',
]

for sql_file in sql_files:
    with open(sql_file, 'r', encoding='utf-8') as file:
        sql_script = file.read()
        # 将 SQL 语句按分号拆分
        sql_statements = sql_script.split(';')
        for statement in sql_statements:
            statement = statement.strip()  # 去除前后空白
            if statement:  # 确保语句非空
                cursor.execute(statement)

# 提交更改并关闭连接
conn.commit()
cursor.close()
conn.close()

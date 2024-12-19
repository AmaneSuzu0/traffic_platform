import pandas as pd
import mysql.connector

# 读取CSV文件，忽略第一列（Unnamed: 0）
data = pd.read_csv('../dataset/qingdao_taxi_data_cleaned_converted.csv', usecols=lambda column: column not in ['Unnamed: 0'])

# 提取唯一的车牌号
unique_taxi_names = data['CLBH'].drop_duplicates()

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    password="naideli2233",  # 数据库密码
    database="db_traffic_platform"  # 数据库名
)

mycursor = mydb.cursor()

# 构建插入语句
sql = "INSERT INTO taxi_info (`taxi_name`) VALUES (%s)"

# 使用executemany批量插入数据
values = [(taxi_name,) for taxi_name in unique_taxi_names]

# 执行插入语句
batch_size = 1000  # 设置每批处理的记录数
for i in range(0, len(values), batch_size):
    mycursor.executemany(sql, values[i:i + batch_size])
    mydb.commit()  # 每批提交一次

mycursor.close()
mydb.close()
import pandas as pd
import mysql.connector
import datetime
import re

# 读入.xlsx文件，并保存为.csv文件
# data = pd.read_excel('dataset/qingdao_taxi_data.xlsx')
# data.to_csv('dataset/qingdao_taxi_data.csv', index=True)

# data = pd.read_csv('dataset/qingdao_taxi_data.csv')
#
# # 保留的列名(仅保留：车辆编号、精确经度、精准纬度、GPS速度、方向、GPS时间、BC时间、载客状态)
# columns_to_keep = ['CLBH', 'JDZB', 'WDZB', 'GPSSD', 'FX', 'GPSSJ', 'BCSJ', 'ZKZT']
# cleaned_data = data[columns_to_keep]
# cleaned_data.to_csv('dataset/qingdao_taxi_data_cleaned.csv', index=True)


# 定义函数，将GPSSJ和BCSJ列的时间格式转换为datetime格式
def convert_time_format(time_str):
    if isinstance(time_str, str):
        try:
            # 将整个字符串中的 "-" 前的空格去掉
            time_str = re.sub(r'\s*-\s*', '-', time_str.strip())

            # 处理日期和时间的部分
            parts = time_str.split(' ')
            date_str = parts[0]  # 获取日期部分
            time_str_full = parts[1]  # 获取时间部分

            # 分割日期部分
            date_parts = date_str.split('-')
            if len(date_parts) == 3:
                day = int(date_parts[0].strip())  # 日
                month_chinese = date_parts[1].strip()  # 月
                year_last_two_digits = int(date_parts[2].strip())  # 年的最后两位
                year = 2000 + year_last_two_digits  # 转换成年份

                # 将中文月份转换为数字
                month_dict = {'1月': 1, '2月': 2, '3月': 3, '4月': 4, '5月': 5, '6月': 6,
                              '7月': 7, '8月': 8, '9月': 9, '10月': 10, '11月': 11, '12月': 12}
                month = month_dict.get(month_chinese)

                # 解析时间部分
                time_parts = time_str_full.split('.')
                hour = int(time_parts[0])  # 小时
                minute = int(time_parts[1])  # 分钟
                second = int(time_parts[2])  # 秒

                # 创建 datetime 对象
                return datetime.datetime(year, month, day, hour, minute, second)
            else:
                print(f"日期格式不正确: {date_str}")
                return None
        except Exception as e:
            print(f"处理时间 {time_str} 时出现错误: {e}")
            return None
    return time_str


# 读取数据并应用转换
data = pd.read_csv('../dataset/qingdao_taxi_data_cleaned.csv')
data['GPSSJ'] = data['GPSSJ'].apply(convert_time_format)
data['BCSJ'] = data['BCSJ'].apply(convert_time_format)

# 保存数据
data.to_csv('../dataset/qingdao_taxi_data_cleaned_converted.csv', index=True)
# 查看前几行数据
print(data.head())

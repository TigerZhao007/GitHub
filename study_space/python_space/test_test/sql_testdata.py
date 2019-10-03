
# ########################################
'''导入功能模块'''
# ########################################
import sqlalchemy
import pandas as pd
import numpy as np
import sqlalchemy
import moment
# ########################################
'''导入数据库连接'''
# ########################################
engine_postgresql = sqlalchemy.create_engine("postgresql://postgres:123456@106.12.30.122:5432/testdb", pool_size=20, max_overflow=5 )

# ########################################
'''设置文件路径 '''
# ########################################
path = r'D:\Desktop\SQL测试题目\testdata_sql.xlsx'

# ########################################
'''循环遍历读取本地文件，修改变量类型，写入数据库 '''
# ########################################
# # 1）获取Excel表中所有sheet的名称
table_names = pd.ExcelFile(path)
table_names = table_names.sheet_names
# table_names = ['A_B001', 'A_B002', 'A_B003', 'A_B004', 'A_B005', 'A_B006',
#                'A_B007', 'A_B008', 'A_B009', 'A_B010', 'A_B011', 'A_B012']
# # 2）遍历读取所有sheet表，并保存到数据库中
for name in table_names:
    print('正在处理数据表：' + name + '......')

    # 3）读取数据表格的文件
    df_temp = pd.read_excel(path, sheet_name=name)

    # 3）处理变量类型
    for keys in df_temp.dtypes[df_temp.dtypes=='datetime64[ns]'].keys():
        if keys != 'update':
             df_temp[keys] = df_temp[keys].apply(lambda x:x.date())
        else:
            pass

    # 4）写入数据库
    with engine_postgresql.connect() as conn:
        df_temp.to_sql(name, conn, if_exists='append', index=False)
        del df_temp

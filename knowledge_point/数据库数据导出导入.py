# -*- coding: utf-8 -*-
"""
时间：2019-11-16
作者: zuoshao（佐少）
代码说明：日期处理
"""

# 导入数据库连接模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd
import setup
import pickle

# ######################################################################################################################
'''路径准备'''
# ######################################################################################################################

# 设置桌面路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_desktop():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
    return desktop_path

path = get_desktop()

# 新加存储路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mkdir(path):

    import os    # 引入模块

    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    isExists = os.path.exists(path)  # 判断路径是否存在, 存在-True, 不存在-False

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录, 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

# 定义要创建的目录
mkpath1 = path + '\\data\\xlsx'
mkpath2 = path + '\\data\\pickle'

# 调用函数
mkdir(mkpath1)
mkdir(mkpath2)

# 更换为存储路径
path1 = path + '\\data\\xlsx'
path2 = path + '\\data\\pickle'

# ######################################################################################################################
'''数据导出'''
# ######################################################################################################################

# 获取数据库所有的表名称~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_db_tablename(link):
    sql = '''select * from pg_tables where schemaname = 'public' '''
    with link as conn:
        pg_tablename_all = pd.read_sql_query(sql, conn)
        pg_tablename_all = tuple(pg_tablename_all['tablename'])

    return pg_tablename_all

pg_tablename_all = get_db_tablename(link = setup.engine_postgresql.connect())

# 导出数据库所有表数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

for i, tablename in zip(range(len(pg_tablename_all)), pg_tablename_all):
    print('正在处理。。。。', i+1, '----', tablename)

    # 数据的读取
    sql = '''select * FROM public."%s"''' %(tablename)
    with setup.engine_postgresql.connect() as conn:
        df_temp = pd.read_sql_query(sql, conn)

    # 数据导出为xlsx文件
    # df_temp.to_excel(path1 + '\\%s.xlsx' % (tablename), index=False)

    # 数据的导出为pickle文件
    with open(path2+ '\\%s' % (tablename), 'wb') as fw:
        pickle.dump(df_temp, fw)

# ######################################################################################################################
'''数据导入'''
# ######################################################################################################################

path1 = r'D:\Desktop\out_data_1108\xlsx\xlsx'
path2 = r'D:\Desktop\out_data_1108\pickle\pickle'

# 获取制定文件夹所有的表名称~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # 方式1：os.listdir(path1)
import os
name_list1 = os.listdir(path1)
name_list2 = os.listdir(path2)

# 方式2：os.walk(file_dir)
def file_name(file_dir):
    ''' 模块os中的walk()函数可以遍历文件夹下所有的文件。 '''
    import os
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))

    return L

# name_list1 = file_name(file_dir=path1)
# name_list2 = file_name(file_dir=path2)

# 获取制定文件夹所有的表名称~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 以pickle处理

name_list2 = ['A_C021', 'A_C021_01', 'A_C022', 'A_C023', 'A_C023_01', 'A_C024', 'A_C025', 'A_C026', 'A_C027', 'A_C028']

for tablename in name_list2:

    print('正在处理表：%s......'%(tablename))
    # 从本地读取数据
    with open(path2 + '\\' + tablename, 'rb') as fr:
        df_temp = pickle.load(fr)

    # 处理变量类型（如果变量类型是时间格式，需要转化为date）
    for keys in df_temp.dtypes[df_temp.dtypes=='datetime64[ns, UTC]'].keys():
        df_temp[keys] = df_temp[keys].apply(lambda x: x.date())


    # # 处理变量类型（如果变量类型是时间格式，需要转化为date）
    # for keys in df_temp.dtypes[df_temp.dtypes=='float64'].keys():
    #     df_temp[keys] = df_temp[keys].apply(lambda x: abs(x))

    # 将数据导入SQL
    with setup.engine_postgresql.connect() as conn:
        df_temp.to_sql(tablename, conn, if_exists='replace', index=False)

# 以Excel处理
for tablename in name_list1:

    print('正在处理表：%s......'%(tablename))
    # 从本地读取数据
    df_temp = pd.read_excel(path1 + '\\' + tablename, sheet_name='Sheet1')

    # 处理变量类型（如果变量类型是时间格式，需要转化为date）
    for keys in df_temp.dtypes[df_temp.dtypes=='datetime64[ns, UTC]'].keys():
        df_temp[keys] = df_temp[keys].apply(lambda x: x.date())

    tablename_temp = tablename.replace('.xlsx', '')
    # 将数据导入SQL
    with setup.engine_postgresql01.connect() as conn:
        df_temp.to_sql(tablename_temp, conn, if_exists='replace', index=False)


# -*- coding: utf-8 -*-
"""
时间：2019-11-16
作者: zuoshao（佐少）
代码说明：日期处理
"""

# 导入数据库连接模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pickle
import pandas as pd

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
mkpath = path + '\\data'

# 调用函数
mkdir(mkpath)

# 更换为存储路径
path = path + '\\data'

# 创建测试数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
dataList = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
dataDic = {0: [1, 2, 3, 4], 1: ('a', 'b'), 2: {'c': 'yes', 'd': 'no'}}
datadf = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [2, 4, 5, 6, 7, 8]})

# 数据序列化到文件中（dump()）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fw = open(path + '\\dataFile', 'wb')

pickle.dump(dataList, fw, -1)   # Pickle the list using the highest protocol available.
pickle.dump(dataDic, fw)   # Pickle dictionary using protocol 0.

fw.close()

# 数据从文件中序列化读出（load()）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# pickle中有几个变量，可以load几次，超过次数会报错
fr = open(path + '\\dataFile', 'rb')

data1 = pickle.load(fr)
data2 = pickle.load(fr)

fr.close()

# pickle数据导出导入操作实例~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tablename = 'datadf'

# 数据的导出
with open(path + '\\%s' %(tablename), 'wb') as fw:
    pickle.dump(datadf, fw)

# 数据的导入
with open(path + '\\%s' %(tablename), 'rb') as fr:
    df_temp = data1 = pickle.load(fr)


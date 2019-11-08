
# 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import time

# 设置桌面路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_desktop():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
    return desktop_path

path = get_desktop()

# 获取当前路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
try:
    FilePath = os.path.dirname(os.path.abspath('__file__')) + '\project\project_total\\'
except:
    FilePath = os.path.dirname(os.path.abspath('__file__'))

# 运行代码设定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
filename_list = ['test01.py', 'test02.py', 'test03.py', 'test04.py',  'test05.py']

# 运行代码设定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 设定存储运行成功或者失败的文件
import pandas as pd
dict_temp = {'run_file': [], 'run_time': [], 'run_type': []}

for filename in filename_list:

    # 设置开始时间
    time_start = time.time()

    # 运行文件
    print('正在处理文件%s......'%(filename))
    a = os.system("python %s%s" % (FilePath, filename))  # 打印执行结果 0表示 success ， 1表示 fail
    if a == 0:
        dict_temp['run_type'] = dict_temp['run_type'] + ['运行成功']

    else:
        dict_temp['run_type'] = dict_temp['run_type'] + ['运行失败']

    # 设置结束时间
    time_end = time.time()
    time_use = "总耗时： %.2f 秒" % (time_end-time_start)

    # 记录运行时间
    dict_temp['run_file'] = dict_temp['run_file'] + [filename]
    dict_temp['run_time'] = dict_temp['run_time'] + [time_use]

# 将运行状态转化为数据框
run_status = pd.DataFrame(dict_temp)
run_status.to_excel(path+'\\run_status.xlsx', sheet_name="Sheet1")


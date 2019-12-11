
def run_main(filename_list, FilePath, logName='run_status_log1'):
    print('正在处理任务：%s ......' %(logName))

    # 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import os
    import time
    import sqlalchemy

    # PostgreSQL连接~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    engine_postgresql00 = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" %
                                                   ('postgres', '123456', '47.100.173.196', '5432', 'test'),
                                                   pool_size=20, max_overflow=5)

    # 运行代码设定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 设定存储运行成功或者失败的文件
    import pandas as pd
    dict_temp = {'run_file': [], 'run_time': [], 'run_type': []}

    for filename in filename_list:

        # 设置开始时间
        time_start = time.time()

        # 运行文件
        print('正在处理文件%s......' % (filename))

        try:
            a = os.system("python %s/%s" % (FilePath, filename))  # 打印执行结果 0表示 success ， 1表示 fail
            if a == 0:
                dict_temp['run_type'] = dict_temp['run_type'] + ['运行成功']
            else:
                dict_temp['run_type'] = dict_temp['run_type'] + ['运行失败']

        except:
            dict_temp['run_type'] = dict_temp['run_type'] + ['运行失败']

        # 设置结束时间
        time_end = time.time()
        time_use = "总耗时： %.2f 秒" % (time_end-time_start)

        # 记录运行时间
        dict_temp['run_file'] = dict_temp['run_file'] + [filename]
        dict_temp['run_time'] = dict_temp['run_time'] + [time_use]

    # 将运行状态转化为数据框
    run_status = pd.DataFrame(dict_temp)
    run_status['updata_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    with engine_postgresql00.connect() as conn:
        run_status.to_sql(logName, conn, if_exists='append', index=False)

def run_main01(filename_list, FilePath):
    print('正在处理任务：%s ......' %('run_main01'))

    # 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import os
    import time
    import sqlalchemy

    # PostgreSQL连接~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    engine_postgresql00 = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" %
                                                   ('postgres', '123456', '47.100.173.196', '5432', 'test'),
                                                   pool_size=20, max_overflow=5)

    # 运行代码路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # FilePath = r'D:/Work/GitHub/centos_deploy/ana02/'
    # FilePath = r'/root/GitHub/centos_deploy/ana02/'

    # 运行代码设定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # filename_list = ['date2db01.py', 'date2db02.py', 'date2db03.py']
    filename_list = ['date2db01.py', 'date2db02.py']

    # 运行代码设定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 设定存储运行成功或者失败的文件
    import pandas as pd
    dict_temp = {'run_file': [], 'run_time': [], 'run_type': []}

    for filename in filename_list:

        # 设置开始时间
        time_start = time.time()

        # 运行文件
        print('正在处理文件%s......' % (filename))

        try:
            # a = os.system("python %s\\%s" % (FilePath, filename))  # 打印执行结果 0表示 success ， 1表示 fail
            a = os.system("python %s/%s" % (FilePath, filename))  # 打印执行结果 0表示 success ， 1表示 fail
            if a == 0:
                dict_temp['run_type'] = dict_temp['run_type'] + ['运行成功']
            else:
                dict_temp['run_type'] = dict_temp['run_type'] + ['运行失败']

        except:
            dict_temp['run_type'] = dict_temp['run_type'] + ['运行失败']

        # 设置结束时间
        time_end = time.time()
        time_use = "总耗时： %.2f 秒" % (time_end-time_start)

        # 记录运行时间
        dict_temp['run_file'] = dict_temp['run_file'] + [filename]
        dict_temp['run_time'] = dict_temp['run_time'] + [time_use]

    # 将运行状态转化为数据框
    run_status = pd.DataFrame(dict_temp)
    run_status['updata_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    with engine_postgresql00.connect() as conn:
        run_status.to_sql('run_status_log', conn, if_exists='append', index=False)


def run_main02(filename_list, FilePath):
    print('正在处理任务：%s ......' %('run_main02'))

    # 导入所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import os
    import time
    import sqlalchemy

    # PostgreSQL连接~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    engine_postgresql00 = sqlalchemy.create_engine("postgresql://%s:%s@%s:%s/%s" %
                                                   ('postgres', '123456', '47.100.173.196', '5432', 'test'),
                                                   pool_size=20, max_overflow=5)

    # 运行代码路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # FilePath = r'D:/Work/GitHub/centos_deploy/ana02/'
    # FilePath = r'/root/GitHub/centos_deploy/ana02/'

    # 运行代码设定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    filename_list = ['date2db03.py']
    # filename_list = ['date2db01.py', 'date2db02.py']

    # 运行代码设定~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # 设定存储运行成功或者失败的文件
    import pandas as pd
    dict_temp = {'run_file': [], 'run_time': [], 'run_type': []}

    for filename in filename_list:

        # 设置开始时间
        time_start = time.time()

        # 运行文件
        print('正在处理文件%s......' % (filename))

        try:
            # a = os.system("python %s\\%s" % (FilePath, filename))  # 打印执行结果 0表示 success ， 1表示 fail
            a = os.system("python %s/%s" % (FilePath, filename))  # 打印执行结果 0表示 success ， 1表示 fail
            if a == 0:
                dict_temp['run_type'] = dict_temp['run_type'] + ['运行成功']
            else:
                dict_temp['run_type'] = dict_temp['run_type'] + ['运行失败']

        except:
            dict_temp['run_type'] = dict_temp['run_type'] + ['运行失败']

        # 设置结束时间
        time_end = time.time()
        time_use = "总耗时： %.2f 秒" % (time_end-time_start)

        # 记录运行时间
        dict_temp['run_file'] = dict_temp['run_file'] + [filename]
        dict_temp['run_time'] = dict_temp['run_time'] + [time_use]

    # 将运行状态转化为数据框
    run_status = pd.DataFrame(dict_temp)
    run_status['updata_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    with engine_postgresql00.connect() as conn:
        run_status.to_sql('run_status_log', conn, if_exists='append', index=False)




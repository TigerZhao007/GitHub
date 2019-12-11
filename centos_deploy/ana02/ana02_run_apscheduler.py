# -*- coding: utf-8 -*-

# 导入系统所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import sys

# 导入需要运行的自定义模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main函数文件所在的位置，这里主要用于导入主函数程序，注意用'/'，方便Linux系统部署
# path = r'D:/Work/GitHub/centos_deploy/ana02/'
path = r'/root/GitHub/centos_deploy/ana02/'

sys.path.append(os.path.dirname(path))

from ana02_run_main import run_main
# from ana02_run_main import run_main01
# from ana02_run_main import run_main02

# 不同任务运行的文件~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main函数运行的文件所对应的路径，这里用户主函数方法中参数设置。
# FilePath = r'D:/Work/GitHub/centos_deploy/ana02/'
FilePath = r'/root/GitHub/centos_deploy/ana02/'

# 不同任务对应的处理文件。
filename_list1 = ['date2db01.py', 'date2db02.py']
filename_list2 = ['date2db03.py']

# 配置定时任务~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':

    scheduler = BlockingScheduler()

    # 任务1：每15秒执行一次
    scheduler.add_job(run_main, 'interval', seconds=15, id='my_job1',
                      kwargs={'FilePath': FilePath, 'filename_list': filename_list1, 'logName': 'run_status_log1'})
    # 任务2：每5分钟执行一次
    scheduler.add_job(run_main, 'interval', minutes=5, id='my_job2',
                      kwargs={'FilePath': FilePath, 'filename_list': filename_list1, 'logName': 'run_status_log2'})

    # scheduler.add_job(run_main, 'cron', hour=15, minute=13)    # 每天的19：23 分执行任务
    # scheduler.add_job(run_main, 'cron', hour='0-23')    # 每天的每小时分执行任务
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


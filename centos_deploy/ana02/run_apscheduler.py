# -*- coding: utf-8 -*-

# 导入系统所需要的模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import sys

# 导入需要运行的自定义模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# path = r'D:/Work/GitHub/centos_deploy/ana02/'
path = r'/root/GitHub/centos_deploy/ana02/'

# sys.path.append(os.path.dirname(os.path.abspath('__file__')))
sys.path.append(os.path.dirname(path))

from run_main import run_main

# 配置定时任务~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(run_main, 'interval', seconds=15)   # 每3秒执行一次
    # scheduler.add_job(run_main, 'cron', hour=15, minute=13)    # 每天的19：23 分执行任务
    # print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass


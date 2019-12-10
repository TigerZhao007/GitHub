
# 转载于：https://mp.weixin.qq.com/s/TTUFQRQ_DiKktJ5-J8O8Pg
# 参考与：https://blog.csdn.net/jingOlivia/article/details/81170969
# 原作者： 清如許 somenzz 2018-10-13

# 前言~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
说到定时任务，你会想起 linux 自带的 crontab ，windows 自带的任务计划，都可以实现守时任务。
没错，操作系统基本都会提供定时任务的实现，但是如果你想要更加精细化的控制，或者说任务程序需要跨平台运行，
最好还是自己实现定时任务框架，Python 的 apscheduler 提供了非常丰富而且方便易用的定时任务接口。
本文介绍如何使用 apscheduler 实现你的定时任务。

apscheduler 使用起来十分方便。提供了基于日期、固定时间间隔以及crontab 类型的任务，
我们可以在主程序的运行过程中快速增加新作业或删除旧作业，如果把作业存储在数据库中，那么作业的状态会被保存，
当调度器重启时，不必重新添加作业，作业会恢复原状态继续执行。apscheduler 可以当作一个跨平台的调度工具来使用，
可以做为 linux 系统crontab 工具或 windows 计划任务程序的替换。注意，apscheduler 不是一个守护进程或服务，
它自身不带有任何命令行工具。它主要是要在现有的应用程序中运行，
也就是说，apscheduler 为我们提供了构建专用调度器或调度服务的基础模块。
'''

# 安装
'''
pip install apscheduler
'''

# 基本概念~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
触发器（triggers）：触发器包含调度逻辑，描述一个任务何时被触发，按日期或按时间间隔或按 cronjob 表达式三种方式触发。
每个作业都有它自己的触发器，除了初始配置之外，触发器是完全无状态的。

作业存储器（job stores）：作业存储器指定了作业被存放的位置，默认情况下作业保存在内存，也可将作业保存在各种数据库中，
当作业被存放在数据库中时，它会被序列化，当被重新加载时会反序列化。作业存储器充当保存、加载、更新和查找作业的中间商。
在调度器之间不能共享作业存储。

执行器（executors）：执行器是将指定的作业（调用函数）提交到线程池或进程池中运行，
当任务完成时，执行器通知调度器触发相应的事件。

调度器（schedulers）：任务调度器，属于控制角色，通过它配置作业存储器、执行器和触发器，添加、修改和删除任务。
调度器协调触发器、作业存储器、执行器的运行，通常只有一个调度程序运行在应用程序中，
开发人员通常不需要直接处理作业存储器、执行器或触发器，配置作业存储器和执行器是通过调度器来完成的。
'''

# 调度器的工作流程
# https://mmbiz.qpic.cn/mmbiz_png/EnE7vpEWFnp7wVByPT7RWZWRkTFp9Ln7g2EfJs0M4ygehLSLI4dvxjn0IooAIYyahSM46jfWlHrENibF5Ay1erw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1

# 实例1 -间隔性任务（BlockingScheduler阻塞型）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -*- coding: utf-8 -*-
# Time: 2018/10/13 19:01:30
# File Name: ex_interval.py

from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

'''
说明：
第 1 行：代码声明文件内容以 utf-8 编码，告诉Python 解释器以 utf-8 编码解析源代码文件。
第 2 行：导入 datetime 模块，用于打印当前时间。导入 os 模块，用于判断操作系统类型。
第 3 行：导入调度器模块 BlockingScheduler，这是最简单的调度器，调用 start 方阻塞当前进程，如果你的程序只用于调度，
         除了调度进程外没有其他后台进程，那么请用 BlockingScheduler 非常有用，此时调度进程相当于守护进程。
第 4 行：定义一个函数 tick 代表我们要调度的作业程序。
第 5 行：实例化一个 BlockingScheduler 类，不带参数表明使用默认的作业存储器-内存，默认的执行器是线程池执行器，
         最大并发线程数默认为 10 个（另一个是进程池执行器）。
第 11 行：添加一个作业 tick，触发器为 interval，每隔 3 秒执行一次，另外的触发器为 date，cron。date 按特定时间点触发，
          cron 则按固定的时间间隔触发。
第 12 行：加入捕捉用户中断执行和解释器退出异常，pass 关键字，表示什么也不做。
'''

# 实例2 - cron 任务（BlockingScheduler阻塞型）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# -*- coding: utf-8 -*-
# Time: 2018/10/13 19:21:09
# File Name: ex_cron.py


from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour=19,minute=23)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

'''
说明：
定时 cron 任务也非常简单，直接给触发器 trigger 传入 'cron' 即可。hour =19 ,minute =23 这里表示每天的19：23 分执行任务。

这里可以填写数字，也可以填写字符串：
hour =19 , minute =23
hour ='19', minute ='23'
minute = '*/3' 表示每 5 分钟执行一次
hour ='19-21', minute= '23' 表示 19:23、 20:23、 21:23 各执行一次任务

# 添加任务作业，args()中最后一个参数后面要有一个逗号，本任务设置在每天凌晨1:00:00执行
scheduler.add_job(task, 'cron', hour='1', minute='0', second='0', args=("hello",))

# 本任务运行在： the third Friday of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
sched.add_cron_job(job_function, month='6-8,11-12', day='3rd fri', hour='0-3')
'''

# 时间设置参数解读：
'''
year	4-digit year number
month	month number (1-12)
day	day of the month (1-31)
week	ISO week number (1-53)
day_of_week	number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
hour	hour (0-23)
minute	minute (0-59)
second	second (0-59)
'''

# 配置调度器~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 启动调度器~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 调度器事件监听~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~















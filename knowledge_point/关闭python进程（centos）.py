

# flask模型部署

# ######################################################################################################################
# Windows系统
# ######################################################################################################################
## pycharm解决关闭flask后依旧可以访问服务
'''
这种问题一般是退出flask服务时选择了disconected而不是选择terminate，
dicconected是一种伪断开，只是在pycharm这里中止了，但是python解释器依旧在运行这个服务。

》解决方式1：
settings > appearance&behavior > system settings > on closing tool with runing process > teminate process

》解决方式2：
如果已经手贱点了disconnect，那么一种好方法是直接在任务管理器结束python解释器。<br>
但是实际情况下我们还是只关闭运行flask的python解释器就行了<br>
1.1、利用cmd关闭监听这个解释器就行<br>
'''

'''python
netstat -ano | findstr 5000
'''
# 一般flask启动时监听的是5000端口，如果修改的话更改后面的端口号:out put<br>
# TCP 127.0.0.1:5000 0.0.0.0:0    listening   13384(进程编号）<br>

# 1.2、找到该进程的PID 这里是13384，然后利用下面命令把它结束掉。<br>
'''python
taskkill /pid XXXXX /f
'''

# ######################################################################################################################
# Centos系统
# ######################################################################################################################

# python后台始终运行python文件~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# nohup /root/anaconda3/bin/python3 /root/GitHub/study_space/knowledge_flask/flask01/app_main.py &

# 关闭后台运行~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 查看指定程序进程
# ps aux |grep httpd
# ps aux |grep python
'''
root      2091  0.0  0.1   5488  2832 ?        Ss   17:19   0:00 /web/apache//bin/httpd -k restart
daemon    2475  0.0  0.1 283220  2256 ?        Sl   17:45   0:00 /web/apache//bin/httpd -k restart
daemon    2476  0.0  0.1 283220  2260 ?        Sl   17:45   0:00 /web/apache//bin/httpd -k restart
daemon    2477  0.0  0.1 283220  2260 ?        Sl   17:45   0:00 /web/apache//bin/httpd -k restart
root      2738  0.0  0.0   5500   736 pts/0    S+   17:56   0:00 grep httpd
'''

# 关闭指定进程
# kill - 9 2091



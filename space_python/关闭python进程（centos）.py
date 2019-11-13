
# 查看指定程序进程
# ps aux |grep httpd
'''
root      2091  0.0  0.1   5488  2832 ?        Ss   17:19   0:00 /web/apache//bin/httpd -k restart
daemon    2475  0.0  0.1 283220  2256 ?        Sl   17:45   0:00 /web/apache//bin/httpd -k restart
daemon    2476  0.0  0.1 283220  2260 ?        Sl   17:45   0:00 /web/apache//bin/httpd -k restart
daemon    2477  0.0  0.1 283220  2260 ?        Sl   17:45   0:00 /web/apache//bin/httpd -k restart
root      2738  0.0  0.0   5500   736 pts/0    S+   17:56   0:00 grep httpd
'''

# 关闭指定进程
# kill - 9 2091




# ######################################################################################################################
# content_text发送纯文本
'''
先从最简单的发送纯文本的邮件开始，调通发送邮件的代码。
以腾讯的企业邮箱为例，smtp_host是发送邮箱的smtp服务地址，不同的邮箱不太一样。
smtp_host:smtp.exmail.qq.com
smtp_port:465
QQ邮箱 POP3 和 SMTP 服务器地址设置如下：邮箱POP3服务器(端口110)SMTP服务器(端口25)
qq.com
pop.qq.com
smtp.qq.com SMTP服务器需要身份验证
'''
import zmail

mail = {
    'subject': '邮件主题：Success!',  # Anything you want.
    'content_text': '邮件正文内容：This message from zmail! QQ交流群:717225969 ',  # Anything you want.
}

server = zmail.server('3447673917@qq.com',
                      'znhkybqfmrwncjca',
                      smtp_host="smtp.qq.com",
                      smtp_port=465)
# server.send_mail(['1432467203@qq.com'], mail)  # 接收着
server.send_mail('1432467203@qq.com', mail)  # 接收着

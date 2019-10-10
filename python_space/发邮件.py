
# ######################################################################################################################
# content_text发送纯文本
'''
先从最简单的发送纯文本的邮件开始，调通发送邮件的代码。以腾讯的企业邮箱为例，smtp_host是发送邮箱的smtp服务地址，
不同的邮箱不太一样。 （smtp_host:smtp.exmail.qq.com； smtp_port:465）
QQ邮箱 POP3 和 SMTP 服务器地址设置如下：邮箱POP3服务器(端口110)SMTP服务器(端口25) （qq.com； pop.qq.com）
smtp.qq.com SMTP服务器需要身份验证
'''
# ######################################################################################################################

import zmail

# 编写邮箱信息（主题+正文）
mail = {
    'subject': '邮件主题：Success!',  # 邮件主题
    'content_text': '邮件正文内容：This message from zmail! QQ交流群:717225969 ',  # 邮件正文
      }

# 编写发邮箱服务（发件人账户+密码等信息）
server = zmail.server('3447673917@qq.com',     # 发件人邮箱号码，该邮箱号码需要开通POP3 和 SMTP 服务。
                      'znhkybqfmrwncjca',      # 发件人邮箱验证信息（不是邮箱密码），该验证信息在开通服务时提供。
                      smtp_host="smtp.qq.com",  # 发件邮箱服务地址，不同服务其不相同
                      smtp_port=465)           # 发件邮箱端口号码，不同服务其不行通

# 编写收件人相关信息（收件人账户等）
server.send_mail('1432467203@qq.com', mail)  # 第一个参数是接受人邮箱号码，第二个参数是邮件信息。





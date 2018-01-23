# -*- coding: utf-8 -*-
"""
@Time: 2018/1/23
@Author: songhao
@微信公众号: zeropython
@File: mail_imge.py
"""
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
辛苦码字不易，能不能点击下广告
"""
#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#sender_qq为发件人的qq号码
sender_qq = 'xxxx@qq.com'
#pwd为qq邮箱的授权码
pwd = 'uvhxrahsxqxxzqjebh'
#发件人的邮箱
sender_qq_mail = 'xxx@qq.com'
#收件人邮箱
receiver = 'xxx@gmail.com'

# 邮件的正文内容
mail_content = ""
# 邮件标题
mail_title = 'zeropython'

# 邮件正文内容
# msg = MIMEMultipart()
msg = MIMEMultipart('related')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
## 接收者的别名
msg["To"] = Header("zeropython接受者", 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msg.attach(msgAlternative)

# 邮件正文内容
mail_body = """
 <p>你好，zeropython 邮件发送测试...</p>
 <p>这是使用python登录qq邮箱发送HTML格式和图片的测试邮件：</p>
 <p><a href='http://www.168seo.cn'>zeropython</a></p>
 <p>图片演示：</p>
 <p><img src="cid:send_image"></p>
"""

# msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
msgText = (MIMEText(mail_body, 'html', 'utf-8'))
msgAlternative.attach(msgText)

# 指定图片为当前目录
fp = open('meinv.jpeg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<send_image>')
msg.attach(msgImage)

# 构造附件1，传送当前目录下的 attach.txt 文件
att1 = MIMEText(open('attach.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="attach.txt"'
msg.attach(att1)

# ssl登录
smtp = SMTP_SSL(host_server)
# set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

# 发送服务
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
# smtp 退出
smtp.quit()




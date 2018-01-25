# -*- coding: utf-8 -*-
"""
@Time: 2018/1/23
@Author: songhao
@微信公众号: zeropython
@File: Python_send_message_attach.py
"""
import socket
socket.setdefaulttimeout(10)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

_user = "1113081366@qq.com"
_pwd = "uvhxrahsxqzqjebh"
_to = "haotianseo@gmail.com"

# 如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

# ---这是文字部分---
part = MIMEText("乔装打扮，不择手段")
msg.attach(part)

# ---这是附件部分---
"""
# xlsx类型附件  
# part = MIMEApplication(open('foo.xlsx', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
# msg.attach(part)
# """
# # jpg类型附件
# """
# part = MIMEApplication(open('foo.jpg', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.jpg")
# msg.attach(part)
# """
# # pdf类型附件
# """
# part = MIMEApplication(open('foo.pdf', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
# msg.attach(part)
# """
# # mp3类型附件
# """
# part = MIMEApplication(open('foo.mp3', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
# msg.attach(part)

s = smtplib.SMTP("smtp.qq.com", 465)  # 连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()


# def sm(receiver, title, body):
#     host = 'smtp.qq.com'
#     port = 25
#     sender = '1113081366@qq.com'
#     pwd = 'cnuhmatvxpqbbaec'
#
#     msg = MIMEText(body, 'html')
#     msg['subject'] = title
#     msg['from'] = sender
#     msg['to'] = receiver
#
#     s = smtplib.SMTP(host, port)
#     s.login(sender, pwd)
#     s.sendmail(sender, receiver, msg.as_string())
#
#     print('The mail named %s to %s is sended successly.' % (title, receiver))
#
# if __name__ == '__main__':
#     sm('5868037@qq.com',"demo",'sdfdsf')
    # server = smtplib.SMTP(smtp_server, smtp_port)
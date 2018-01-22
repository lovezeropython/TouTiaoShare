# -*- coding: utf-8 -*-
"""
@Time: 2018/1/22
@Author: songhao
@微信公众号: zeropython
@File: send_messages.py
@ website:https://www.168seo.cn
"""
# 导入用到的模块
import socket
import smtplib
import urllib

# 邮箱配置
mail_options = {
    'server':'smtp.qq.com',#使用了QQ的SMTP服务，需要在邮箱中设置开启SMTP服务
    'port':25,             #端口
    'user':'hacker@qq.com',#发送人
    'pwd':'hacker',        #发送人的密码
    'send_to':'sniper@qq.com',  #收件者
}

# 短信平台配置
msg_options={
    'user':'hacker',    #短信平台的用户名
    'pwd':'74110',      #短信平台的密码
    'phone':'12345678910',   #需要发短信的电话号码
}
test_host = 'https://www.168seo.cn'

def url_request(host,port=80):
    """
    :param host: 域名
    :param port: 默认80端口
    :return:
    """
    try:
        response = urllib.urlopen(host)
        response_code = response.getcode()
        if 200 != response_code:
            return response_code
        else:
            return True
    except IOError as e:
            return False



def send_message(msg,host,status):
    """短信发送"""
    send_msg='服务器:%s挂了！状态码：%s' % (host,status)
    request_api="http://www.uoleem.com.cn/api/uoleemApi?username=%s&pwd=%s&mobile=%s&content=%s"  \
            % (msg['user'],msg['pwd'],msg['phone'],send_msg)
    return url_request(request_api)

def send_email(mail,host,status):
    """邮件发送"""
    smtp = smtplib.SMTP()
    smtp.connect(mail['server'], mail['port'])
    smtp.login(mail['user'],mail['pwd'])
    msg="From:%s\rTo:%s\rSubject:服务器: %s 挂了 !状态码:%s\r\n" \
         % (mail['user'],mail['send_to'],host,status)
    smtp.sendmail(mail['user'],mail['send_to'], msg)
    smtp.quit()


if __name__=='__main__':
    status = url_request(test_host)
    if status is not True and status is not None:
        send_email(mail_options,test_host,status)
        send_message(msg_options,test_host,status)
    else:
        pass
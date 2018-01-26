# -*- coding: utf-8 -*-
"""
@Time: 2018/1/26
@Author: songhao
@微信公众号: zeropython
@File: indez.py
@website:https://www.168seo.cn/python/24328.html
"""
# 导入用的模块
import requests
import re

# 获取网站的标题
def get_title(html):
    """"
    :param html: 源代码
    :return: 返回源代码的title
    """
    return re.search("<title>(.*?)</title>", html, re.S).group(1)

# 登录网站
def get_login(url, data):
    """
    :param url: wordpress 后台登录地址
    :param data: post传入的账号密码
    :return: 返回已经登录的Session对象
    """
    s = requests.Session()
    s.post(url, data=data)
    return s

if __name__ == '__main__':
    # 后台登录地址
    login_url = "http://mac-wordpress.test/wp-login.php"
    # 登录的账号密码
    data = {"log":"root",
            "pwd":"root"}
    # 登录wordpress
    s = get_login(login_url, data)

    # 利用session 请求后台的网址
    r =  s.get("http://mac-wordpress.test/wp-admin/upload.php")

    # 获取请求地址的标题
    t = get_title(r.text)

    if "媒体库" in t:
        print("登录成功",t)
    # 根据标题获取是否登录


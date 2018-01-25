#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LostInNight
# @Date:   2015-11-03 18:47:47
# @Last Modified by:   LostInNight
# @Last Modified time: 2015-11-19 15:45:56

# 真实、迅雷、QQ旋风下载地址之间的转换
import base64
import re


'''
原理:
迅雷下载地址："thunder://"+Base64编码("AA"+"真实地址"+"ZZ")
QQ旋风下载地址:"qqdl://"+Base64编码("真实地址")
'''


# 常量定义区 #

THUNDER_HEADER = "thunder://"
THUNDER_PREFIX = "AA"
THUNDER_SUFFIX = "ZZ"
QQ_HEADER = "qqdl://"
ERROR = "传入的URL有误，请检查！"


# 判断url是否有效
def checkUrl(func):
    def wrapper(url):
        if re.match(r"(http|https|ftp|ed2k|thunder|qqdl)://", url):
            return func(url)
        else:
            return ERROR
    return wrapper


@checkUrl
def real2QQ(url):
    url = base64.b64encode(url.encode("utf-8"))
    url = QQ_HEADER + url.decode("utf-8")
    return url


@checkUrl
def qq2Real(url):
    url = url[len(QQ_HEADER):]
    url = base64.b64decode(url.encode("utf-8"))
    url = url.decode("utf-8")
    return url


@checkUrl
def real2Thunder(url):
    url = THUNDER_PREFIX + url + THUNDER_SUFFIX
    url = base64.b64encode(url.encode("utf-8"))
    url = THUNDER_HEADER + url.decode("utf-8")
    return url


@checkUrl
def thunder2Real(url):
    url = url[len(THUNDER_HEADER):]
    url = base64.b64decode(url.encode("utf-8"))
    url = url.decode("utf-8")
    url = url[len(THUNDER_PREFIX):-len(THUNDER_SUFFIX)]
    return url


@checkUrl
def qq2Thunder(url):
    return real2Thunder(qq2Real(url))


@checkUrl
def thunder2QQ(url):
    return real2QQ(thunder2Real(url))


if __name__ == "__main__":
    # 测试用
    th_url ="thunder://QUFmdHA6Ly95Z2R5ODp5Z2R5OEB5ZzQ1LmR5ZHl0dC5uZXQ6NjAzMi9bJUU5JTk4JUIzJUU1JTg1JTg5JUU3JTk0JUI1JUU1JUJEJUIxd3d3LnlnZHk4LmNvbV0uJUU3JThCJTk5JUU1JTg3JUJCJUU3JUIyJUJFJUU4JThCJUIxJUVGJUJDJTlBJUU1JUI3JTg1JUU1JUIzJUIwJUU1JUFGJUI5JUU1JTg2JUIzLkJELjcyMHAuJUU0JUI4JUFEJUU4JThCJUIxJUU1JThGJThDJUU1JUFEJTk3JUU1JUI5JTk1Lm1rdlpa"
    # url_1 = r'ed2k://|file|Supergirl.S01E02.720p.HDTV.X264-DIMENSION.mkv|947617048|5D430BBD720C13598D867C3424B50B8D|h=2AG3ZXRLCWNGC4K5WFNC4QOMVDSXWBBM|/'
    # url_2 = r'd2k://|file|Supergirl.S01E02.720p.HDTV.X264-DIMENSION.mkv|947617048|5D430BBD720C13598D867C3424B50B8D|h=2AG3ZXRLCWNGC4K5WFNC4QOMVDSXWBBM|/'
    # print(real2QQ(url_1))
    # print(thunder2QQ(real2Thunder(url_1)))
    # print(real2QQ(url_2))
    print(thunder2Real(th_url))
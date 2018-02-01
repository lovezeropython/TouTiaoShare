# -*- coding: utf-8 -*-
"""
@Time: 2018/2/1
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""

# 真实、迅雷、QQ旋风下载地址之间的转换
# 原理:迅雷下载地址："thunder://"+Base64编码("AA"+"真实地址"+"ZZ")

# Base64模块
import base64
import re

# 常量定义区 #

THUNDER_HEADER = "thunder://"
THUNDER_PREFIX = "AA"
THUNDER_SUFFIX = "ZZ"
ERROR = "传入的URL有误，请检查！"

# 我们首先判断链接是不是链接

def is_url(func):
    def warpper(url):
        if re.match(r"(http|https|ftp|ed2k|thunder|qqdl)://", url):
            return func(url)
        else:
            return ERROR
    return warpper

@is_url
def thunder2Real(url):
    url = url[len(THUNDER_HEADER):]
    # 把url中的"thunder://"去除

    url = url.encode("utf-8")
    # url 按照utf-8的形式进行编码

    url = base64.b64decode(url)
    # base64 进行编码

    url = url.decode("utf-8")
    # url 进行解码
    url = url[len(THUNDER_PREFIX):-len(THUNDER_SUFFIX)]
    # 去除前缀和后缀
    print( url)

if __name__ == '__main__':
    url = "thunder://QUFmdHA6Ly9kOmRAZHlnb2RqOC5jb206MTIzMTEvWyVFNyU5NCVCNSVFNSVCRCVCMSVFNSVBNCVBOSVFNSVBMCU4Mnd3dy5keTIwMTguY29tXSVFNyU5QiU5NyVFNiVCRCU5QyVFOSVCQiU4NCVFOSU4NyU5MSVFNSU5RiU4RUJEJUU0JUI4JUFEJUU4JThCJUIxJUU1JThGJThDJUU1JUFEJTk3Lm1wNFpa"

    thunder2Real(url)




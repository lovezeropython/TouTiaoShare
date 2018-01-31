# -*- coding: utf-8 -*-
"""
@Time: 2018/1/31
@Author: songhao
@微信公众号: zeropython
@File: new_demo.py
"""

from urllib.parse import quote
import requests
import random
import hashlib

"""
1. 如何申请翻译API服务？
http://developer.baidu.com/

已登录百度账号的用户，点击“立即使用”，注册成为开发者，即可获得APPID和密钥信息；同一个账户或手机号码仅能申请一组APPID和密钥信息，该APPID和密钥信息可用于多项服务调用。

已注册开发者的用户，可通过点击“立即使用”或者在管理控制台开通相应服务；

已开通某项服务的用户，可在管理控制台开通其他服务。
"""

appid = '2016080300004261555'
secretKey = 'WFBCM4JedWddWv9otIOCxMYR'


def get_myurl(words,fromLang='auto',toLang = 'zh'):
    for word in words:
        salt = random.randint(32768, 65536)
        sign = appid + word + str(salt) + secretKey
        myMd5 = hashlib.md5()
        myMd5.update(sign.encode("utf-8"))
        sign = myMd5.hexdigest()
        """
        签名生成方法如下：
        1、将请求参数中的 APPID(appid), 翻译query(q, 注意为UTF-8编码), 随机数(salt), 以及平台分配的密钥(可在管理控制台查看)
        按照 appid+q+salt+密钥 的顺序拼接得到字符串1。
        2、对字符串1做md5，得到32位小写的sign。
        """
        yield '/api/trans/vip/translate'+'?appid='+appid+'&q='+quote(word)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

def get_translate_word(url):
    print('http://api.fanyi.baidu.com' + url)
    try:
        response = requests.get('http://api.fanyi.baidu.com' + url, timeout=5)
        print(response.json())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    words = ['world', 'seo', 'python','zeropython']
    for u in get_myurl(words):
        get_translate_word(u)

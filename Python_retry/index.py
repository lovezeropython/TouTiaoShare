# -*- coding: utf-8 -*-
"""
@Time: 2018/2/3
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""

from requests.exceptions import ConnectTimeout
import requests
from retry import retry

def do_some(url, n=1):
    # 给n一个默认值1
    print(n, url)
    if n > 2:
        # 当n>2的时候就不再去重试了
        print('retry many times')
        return None
    try:
        r = requests.get(url, timeout=3)
        return r.text
    except Exception as e:
        # 返回异常
        print(e.args)
        n += 1
        # 失败 n加一，重试
        return do_some(url, n)

# 第二中方法
from retry import retry
@retry(exceptions=ConnectTimeout, tries=3)
# tries=3 表示重试次数
def do_other(ourl):
    print(ourl, 'ddddddddddd')
    r = requests.get(ourl, timeout=3)
    return r.text



if __name__ == '__main__':
    ourl = "https://www.google.com"
    # 方法1
    do_some(ourl)

    # 方法二
    try:
        do_other(ourl)
    except Exception as e:
        print("dssssssssss")
        pass

# -*- coding: utf-8 -*-
"""
@Time: 2018/1/21
@Author: songhao
@微信公众号: zeropython
@File: get_baidu_real_url.py
@ website: https://www.168seo.cn/python/1204.html
"""



import requests
import urllib.request
bd_url = "https://www.baidu.com/link?url=mhMx_W4kSIqeHdckh0dvrBt4LDIxvTrf1XqoDQKAptW&amp;" \
         "ck=5341.10.0.0.0.203.232.0&amp;shh=www.baidu.com&amp;sht=baiduhome_pg&amp;wd=&amp;" \
         "eqid=cd90b17a00034b1c000000035a645fd5"

r = requests.get(bd_url)
print(r.url)


# python3下和Python2.7 下urlopen 引入不同
r = urllib.request.urlopen(bd_url)

print(r.geturl())

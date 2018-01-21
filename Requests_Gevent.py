# -*- coding: utf-8 -*-
"""
@Time: 2018/1/21
@Author: songhao
@微信公众号: zeropython
@File: Requests_Gevent.py
@ website: https://www.168seo.cn/python/24352.html
"""
import grequests
import json

# 构建urls
urls = ["http://lab.crossincode.com/recite/chap?c={}".format(x) for x in range(1, 11)]

# 请求队列，还未发出请求
rs = (grequests.get(u) for u in urls)

# 批量发出请求，得到响应的列表resps
resps = grequests.map(rs)


def get_words(ht):
    dc = json.loads(ht)
    print(dc['voca'])


for resp in resps:
    # 解析出单词的信息。
    get_words(resp.text)

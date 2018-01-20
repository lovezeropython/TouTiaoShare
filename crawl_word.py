# -*- coding: utf-8 -*-
"""
@Time: 2018/1/19
@Author: songhao
@微信公众号: zeropython
@File: crawl_word.py
"""
import requests
import json
# url = "http://lab.crossincode.com/recite/"
base_url = "http://lab.crossincode.com/recite/chap?c={}"
for x in range(1,11):
    url = base_url.format(x)
    r = requests.get(url)
    print(r.status_code)
    if r.status_code ==200:
        # print(r.text)
        jsons = json.loads(r.text)
        print(jsons['voca'])
        for word in jsons['voca']:
            print(word.get('word'),word.get('explansion'),word.get('expand'))
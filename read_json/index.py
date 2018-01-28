# -*- coding: utf-8 -*-
"""
@Time: 2018/1/28
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""

import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data)

print("dumps".center(31,"*"))
print(json_str)
print(type(json_str))

print("loads".center(31,"*"))
data1 = json.loads(json_str)

print(data1)
print(type(data1))
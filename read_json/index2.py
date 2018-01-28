# -*- coding: utf-8 -*-
"""
@Time: 2018/1/28
@Author: songhao
@微信公众号: zeropython
@File: index2.py
"""

__author__ = 'songhao'
import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

print("dump/load 使用之前".center(30, "*"))
print(data)
print(type(data))

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
    print("dump/load 使用之后".center(30, "*"))
    print(data)
    print(type(data))
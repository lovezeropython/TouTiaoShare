# -*- coding: utf-8 -*-
"""
@Time: 2018/1/18
@Author: songhao
@微信公众号: zeropython
@File: inspect模块.py
"""
import inspect
def hell():
    return "hell"

print(inspect.isfunction(hell))
print(inspect.getmembers(str))
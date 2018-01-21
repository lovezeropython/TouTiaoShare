# -*- coding: utf-8 -*-
"""
@Time: 2018/1/21
@Author: songhao
@微信公众号: zeropython
@File: name_main.py
"""
import random
def get_range():
    return [random.random() for x in range(10)]

if __name__ == '__main__':
    d = get_range()
    print(d)
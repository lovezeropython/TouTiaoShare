# -*- coding: utf-8 -*-
"""
@Time: 2018/1/22
@Author: songhao
@微信公众号: zeropython
@File: trip模块.py
"""
import trip

def main():
    r = yield trip.get('https://httpbin.org/get')
    print(r.content)

trip.run(main)
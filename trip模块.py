# -*- coding: utf-8 -*-
"""
@Time: 2018/1/22
@Author: songhao
@微信公众号: zeropython
@File: trip模块.py
"""
import time, functools
import requests,trip

@trip.coroutine
def main():
    global r
    r = yield trip.get('https://github.com/timeline.json')

trip.run(main)
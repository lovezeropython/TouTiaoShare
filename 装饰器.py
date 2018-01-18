# -*- coding: utf-8 -*-
"""
@Time: 2018/1/18
@Author: songhao
@微信公众号: zeropython
@File: 装饰器.py
"""
"""
装饰器是可调用的对象，其中一个参数就是函数，（函数是一等对象），装饰器可能会处理被装饰的函数，然后将它返回

@decorate
def target():
    print("正在运行 target")
####################
def target():
    print("正在运行 target")

target = decorate(target)

# 这两个写法最终的效果是一致的

"""
fs = []
def get_f(func):
    fs.append(func)
    return func

@get_f
def one():
    print("one")

@get_f
def two():
    print("two")

for x in fs:
    x()




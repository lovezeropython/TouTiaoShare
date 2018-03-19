# -*- coding: utf-8 -*-
"""
@Time: 2018/3/19
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""

#导入timeit.timeit
from timeit import timeit
import time
#看执行1000000次x=1的时间：

print(timeit('x=1'))

#看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
timeit('x=1', number=1)

#看一个列表生成器的执行时间,执行1次：
timeit('[i for i in range(10000)]', number=1)

#看一个列表生成器的执行时间,执行10000次：
timeit('[i for i in range(100) if i%2==0]', number=10000)


# 计算函数的运行时间


def text():
    for x in range(100):
        return x

 # timeit(函数名_字符串，运行环境_字符串，number=运行次数)
d = timeit('text()',"from __main__ import text",number=1)

print(d)

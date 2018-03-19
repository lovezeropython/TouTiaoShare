# -*- coding: utf-8 -*-
"""
@Time: 2018/3/19
@Author: songhao
@微信公众号: zeropython
@File: 装饰器_time.py
"""
import time
def exeTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        print("@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__))
        back = func(*args, **args2)
        print("@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__))
        print ("@%.3fs taken for {%s}" % (time.time() - t0, func.__name__))
        return back
    return newFunc

@exeTime
def test():
    for x in range(100):
        return x

if __name__ == '__main__':
    test()
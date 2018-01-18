# -*- coding: utf-8 -*-
"""
@Time: 2018/1/18
@Author: songhao
@微信公众号: zeropython
@File: 手写一个迭代器.py
"""

class Data():
    # 创建一个可迭代的类
    def __init__(self):
        # 初始化一个变量_new_data 为列表
        self._new_data = []

    def add(self, i):
        # 向 _new_data 变量中添加数据
        self._new_data.append(i)

    def data(self):
         # 让_new_data 变成可迭代的对象
        return iter(self._new_data)


if __name__ == '__main__':
    d = Data()
    d.add(1)
    d.add(2)
    d.add(3)
    for i in d.data():
        print(i)



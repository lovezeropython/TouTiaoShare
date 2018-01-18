# -*- coding: utf-8 -*-
"""
@Time: 2018/1/18
@Author: songhao
@微信公众号: zeropython
@File: 手写一个迭代器.py
"""

class Data():
    def __init__(self):
        self._new_data = []

    def add(self, i):
        self._new_data.append(i)

    def data(self):
        return iter(self._new_data)


if __name__ == '__main__':
    d = Data()
    d.add(1)
    d.add(2)
    d.add(3)
    for i in d.data():
        print(i)



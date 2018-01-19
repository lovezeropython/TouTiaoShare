# -*- coding: utf-8 -*-
"""
@Time: 2018/1/18
@Author: songhao
@微信公众号: zeropython
@File: superclass.py
"""
"""
# 创建一个One类
class One(object):
    def new_one(self):
        print("new_one func")

class Two(One):
    # 创建 Two 继承 One
    def __init__(self):
        super().new_one()
        # 调用 One 类中的 new_one 方法

    def new_two(self):
        print("newtp")
        super().new_one()

if __name__ == '__main__':
    t = Two()
    # 实例化 Two
    t.new_two()
    # 调用new_two


class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def get_x_y(self):
        print(self.x ,self.y)


"""

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
            # Call original __setattr__
        else:
            setattr(self._obj, name, value)

"""
在上面代码中，__setattr__() 的实现包含一个名字检查。 如果某个属性名以下划线(_)开头，就通过 super() 调用原始的 __setattr__() ，
 
否则的话就委派给内部的代理对象 self._obj 去处理。 这看上去有点意思，因为就算没有显式的指明某个类的父类， super() 仍然可以有效的工作。

"""
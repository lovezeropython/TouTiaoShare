# -*- coding: utf-8 -*-
"""
@Time: 2018/1/25
@Author: songhao
@微信公众号: zeropython
@File: namspace.py
@website:https://www.168seo.cn/python/24362.html
"""
"""


def fool():
    print(a)
    print("局部变量", locals())

fool()
print("全局变量", globals())


"""
"""
如果要修改 必须 global a
如果只是简单的读取可以 直接读取
"""

a = "This is a global variable"
# 修改全局变量
def fool():
    global a
    b = "new_b"
    print(a)
    a = "new a"
    print(a)
    print(locals(),"局部变量")

fool()
print(globals(), "全局变量")


"""
# output
Traceback (most recent call last):
  File "/Users/songhao/py/TouTiaoShare/装饰器/namspace.py", line 32, in <module>
    fool()
  File "/Users/songhao/py/TouTiaoShare/装饰器/namspace.py", line 28, in fool
    print(a)
UnboundLocalError: local variable 'a' referenced before assignment
"""
"""
# 添加global，就可以修改了
def fool():
    global a
    a = "new_a"
    print(a)
    print(locals(),"局部变量")

fool()
print(globals(), "全局变量")

"""
# {} 局部变量 因为a不属于 局部变量
# {'__name__': '__main__', '__doc__': '\n@Time: 2018/1/25\n@Author: songhao\n@微信公众号: zeropython\n@File: namspace.py\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x10376a668>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/songhao/py/TouTiaoShare/装饰器/namspace.py', '__cached__': None, 'a': 'new_a', 'fool': <function fool at 0x103cf59d8>} 全局变量
"""
变量的生命周期啊

def fool():
    x = 1

fool()
print(x)


  File "/Users/songhao/py/TouTiaoShare/装饰器/namspace.py", line 62
    global x
    ^
SyntaxError: name 'x' is assigned to before global declaration
"""



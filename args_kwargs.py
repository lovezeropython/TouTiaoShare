# -*- coding: utf-8 -*-
"""
@Time: 2018/1/23
@Author: songhao
@微信公众号: zeropython
@File: args_kwargs.py
"""
""""""
def fun_var_args(farg, *args):
    print("arg:", farg)
    for value in args:
        print("another arg:", value)

# fun_var_args(1, "two", 3,77,99)
# *args可以当作可容纳多个变量组成的list

def fun_var_kwargs(farg, **kwargs):
    print("arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key])  )

# myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary
# fun_var_kwargs(farg=1, myarg2="two", myarg3=3)
def fun_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1 )
    print("arg2:", arg2  )
    print("arg3:", arg3 )

# kk = ["two", 3] #list
#
# fun_var_args_call(1, *kk)


def fun_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1 )
    print("arg2:", arg2 )
    print("arg3:", arg3 )

ff = {"arg3": 3, "arg2": "two"} # dictionary

fun_var_args_call(1, **ff)
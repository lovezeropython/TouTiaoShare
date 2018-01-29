# -*- coding: utf-8 -*-
"""
@Time: 2018/1/29
@Author: songhao
@微信公众号: zeropython
@File: table01.py
"""
from tabulate import tabulate
table = [
    ["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]
        ]
print("表格样式".center(50,'*'))
print(tabulate(table))
print("表格样式".center(50,'*'))
print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))
print("表格样式".center(50,'*'))
print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],headers="firstrow"))
print("表格样式".center(50,'*'))
print(tabulate({"Name": ["Alice", "Bob"],"Age": [24, 19]}, headers="keys"))
headers = ["item", "qty",'dd']
print("表格样式".center(50,'*'))
print(tabulate(table, headers, tablefmt="grid"))
print("表格样式".center(50,'*'))
print(tabulate(table, headers, tablefmt="pipe"))
print("表格样式".center(50,'*'))
print(tabulate(table, headers, tablefmt="orgtbl"))
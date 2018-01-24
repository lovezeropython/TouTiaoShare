# -*- coding: utf-8 -*-
"""
@Time: 2018/1/23
@Author: songhao
@微信公众号: zeropython
@File: pre_table.py
@web:https://www.168seo.cn/python/1726.html
"""
from prettytable import PrettyTable

table = PrettyTable(["key", "search", "cate"])
# 标题

with open('1.csv') as f:
    for line in f:
        row = line.split(',')
        key = row[0]
        search = int(row[1])
        # 一定要转换成数字 不然排序不生效
        cate = row[2]
        table.add_row([key, search, cate])

print(table.get_string(sortby="search", reversesort=True))
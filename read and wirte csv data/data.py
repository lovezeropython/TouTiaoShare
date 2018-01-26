# -*- coding: utf-8 -*-
"""
@Time: 2018/1/26
@Author: songhao
@微信公众号: zeropython
@File: data.py
@ website:https://www.168seo.cn/python/24364.html
"""

# 导入用到的库
import csv
from collections import namedtuple

with open('data.csv', encoding="utf8") as f:
    f_csv = csv.reader(f)
    # 获取csv 表头
    headings = next(f_csv)
    # 映射名称到序列元素
    Row = namedtuple('Row', headings)

    print("表头",headings)
    for r in f_csv:
        row = Row(*r)
        print(row)
        # 可以直接根据下标进行访问
        print(row.支付订单数)


"""
# 另外一个选择就是将数据读取到一个字典序列中去。可以这样做：

import csv
with open('data.csv', encoding="utf-8") as f:
    f_csv = csv.DictReader(f)
    # print(header)
    datas = []
    for row in f_csv:
        print(row.keys())
        datas.append(row)
        # 是一个字典的类型
        print(isinstance(row,dict))
        print(row['支付订单数'])

        /usr/local/bin/python3.6 /Users/songhao/Desktop/data/data.py
        odict_keys(['买家ID', '支付订单数', '客单价', '退货订单数'])
        True
        2

    with open('data2.csv', 'w',encoding='utf-8') as f:
        # 创建一个 writer 对象
        f_csv = csv.writer(f)
        # 写入数据源
        f_csv.writerows(datas)
"""
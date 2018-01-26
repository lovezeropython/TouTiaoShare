# -*- coding: utf-8 -*-
"""
@Time: 2018/1/26
@Author: songhao
@微信公众号: zeropython
@File: d1.py
"""

# 读取csv方式一 因为csv是文本格式的
with open('data.csv', encoding='utf-8') as f:

    for line in f:
        # 读取
        row = line.strip()
        print(row)
        # 存储
        with open('data1.csv','a+',encoding="utf-8") as f:
            # 直接写入
            f.write(row+"\n")



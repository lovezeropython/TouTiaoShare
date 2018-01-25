# -*- coding: utf-8 -*-
"""
@Time: 2018/1/23
@Author: songhao
@微信公众号: zeropython
@File: analysis_data.py
"""
import pandas
from pymongo import MongoClient

"""
创造一个和Mongondb之间的链接
"""

client = MongoClient('localhost', 27017)

db = client.app_db
collection = db.myset
df = pandas.DataFrame(list(collection.find()))
del df['_id']
# print(df)
# print(df.sort_values['discounted_price'])
# df.sort(["discounted_price"])
dd = df.sort_values(["discounted_price"],ascending=True).head(10)
df.to_csv('dsfds.csv', encoding="utf8")
print(dd)
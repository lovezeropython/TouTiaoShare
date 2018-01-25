# -*- coding: utf-8 -*-
"""
@Time: 2018/1/23
@Author: songhao
@微信公众号: zeropython
@File: mac_app.py
"""
from operator import itemgetter
from urllib.parse import urlencode
import requests
import json
from pymongo import MongoClient


# urlencode()
datas = []

def get_html(page):
    data = {
        'platform': 'web',
        'limit': 10,
        'offset': (page-1)*10
    }

    base_url = "http://app.so/api/v5/appso/discount/?"


    r = requests.get(base_url, data=data)

    if r.status_code == 200:
        ht = json.loads(r.text)
        return ht
    return None
def get_data(jsons_data):

    for data in jsons_data['objects']:
        app_data = {
            'content':data['content'],
            'region':data['app']['download_link'][0]['region'],
            'price':data['app']['download_link'][0]['price'],
            'discounted_price':data['discount_info'][0]['discounted_price'],
            'expired': data['discount_info'][0]['expired'],
            'original_price': data['discount_info'][0]['original_price'],
            'download_link': data['app']['download_link'][0]['link'],
        }
        collection.insert(app_data)
        next_link = data.get('meta').get('next',0)
        if next_link:

        # datas.append(app_data)


def main():
    if get_html(1):
        get_data(get_html(1))

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.app_db
    collection = db.myset
    main()


    # # print(datas)
    # rows_by_price = sorted(datas, key=itemgetter('discounted_price'))
    # print(rows_by_price)

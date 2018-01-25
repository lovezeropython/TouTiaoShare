# -*- coding: utf-8 -*-
"""
@Time: 2018/1/23
@Author: songhao
@微信公众号: zeropython
@File: new_mac_app.py
"""

from operator import itemgetter
from urllib.parse import urlencode
import requests
import json
from pymongo import MongoClient

def get_html(url):

    r = requests.get(url)

    if r.status_code == 200:
        ht = json.loads(r.text)
        return ht
    return None

def parse_one_page(jsons_data):

    for data in jsons_data['objects']:
        try:
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
            print("存储完成", app_data)
        except Exception as e:
            print(e)
            pass


    next_link = jsons_data.get('meta').get('next')
    if next_link:
        new_link = "http://app.so"+next_link
        print(new_link)
        main(new_link)


def main(url):
    ht = get_html(url)
    parse_one_page(ht)

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.app_db
    collection = db.myset
    first_page = "http://app.so/api/v5/appso/discount/?platform=web&limit=10&offset=0"
    main(first_page)
    print("全部数据已储存完成")

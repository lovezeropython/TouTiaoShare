# -*- coding: utf-8 -*-
"""
@Time: 2018/2/4
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""
# iask 采集的主文件

# coding:utf-8
import requests, re
from pyquery import PyQuery as pq
from requests.exceptions import RequestException
from fake_useragent import UserAgent
SITE = "http://iask.sina.com.cn"
from bs4 import BeautifulSoup as bs4
from Tools import Tool
import pymongo
from config import *
headers = {
    'User-Agent':UserAgent().chrome,
}
def getHtml(url):
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None

def get_next_url_one(content):
    try:
        return  SITE+bs4(content,"lxml").select('.btn-page')[-1]['href']
    except Exception as e:
        print(e)
        pass


def get_list_href(url):
    html1 = getHtml(url)
    doc = pq(html1)
    for a in doc('.question-title a').items():
        page_url = SITE+a.attr.href
        get_detail_page(page_url)
        print(a.text())

    nex = get_next_url_one(html1)
    print('正在抓取',nex)
    get_list_href(nex)

def get_detail_page(url):
    html = getHtml(url)
    newselect = bs4(html, "lxml").select('pre')
    try:
        title = Tool().replace(newselect[0].text)
        answer = Tool().replace(newselect[1].text)
        save_mongo({'title':title,'answer':answer})
    except Exception as e:
        print(e)
        pass

def save_mongo(dic):
    clent = pymongo.MongoClient(host='localhost',port=27017)
    clent.MONGO_DB.MONGO_TB.insert_one(dic)
    print("正在保存",dic)
    # pass

if __name__ == '__main__':
    url = "http://iask.sina.com.cn/c/213-goodAnswer-180-new.html"
    html = getHtml(url)
    nextii = get_next_url_one(html)
    get_list_href(nextii)
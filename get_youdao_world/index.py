# -*- coding: utf-8 -*-
"""
@Time: 2018/1/29
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""
import requests
from pyquery import PyQuery as pq
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}

def get_word_info(word):
    url = "http://dict.youdao.com/w/eng/{}/".format(word)

    resp = requests.get(url,headers=headers)
    # print(resp.text)
    # PyQuery初始化 html
    doc = pq(resp.text)

    des = ''

    # 遍历翻译
    for li in doc.items('#phrsListTab .trans-container ul li'):
        print(li.text())
        """
        n. 巨蟒；大蟒；丹舌
        n. (Python)人名；(法)皮东  
        """
        des += li.text()

    print({'word': word, '注释': des})
    # {'word': 'Python', '注释': 'n. 巨蟒；大蟒；丹舌n. (Python)人名；(法)皮东'}

if __name__ == '__main__':
    get_word_info('Python')


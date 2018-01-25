# -*- coding: utf-8 -*-
"""
@Time: 2018/1/15
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""
import requests
import time
from pyquery import PyQuery as pq

# 装饰器 获取函数的运行时间
def exeTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        print("@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__))
        back = func(*args, **args2)
        print("@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__))
        print("@%.3fs 同步 taken for {%s}" % (time.time() - t0, func.__name__))
        return back
    return newFunc

def get_data(url):
    """
    Pyquery接卸html
    """
    html = requests.get(url).text
    for item in pq(html)('.item').items():
        title = item.find('.title').html()
        # #  <span class="title">肖申克的救赎</span><span class="title"> / The Shawshank Redemption</span>
        # #  返回第一个 .title里面的内容
        num = item.find('.pic em').text()
        star = item.find('.rating_num').text()
        img = item.find('.pic a img').attr('src')
        print(title, star, num, img)
# 获取信息
@exeTime
def get_all(urls):
    for url in urls:
        get_data(url)

if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start=%s'%str(page_num) for page_num in range(0, 250 ,25)]
    # print(urls)
    get_all(urls)
# @2.079s taken for {get_all}



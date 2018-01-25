# -*- coding: utf-8 -*-
"""
@Time: 2018/1/15
@Author: songhao
@微信公众号: zeropython
@File: index.py
@ website:www.168seo.cn
"""
import requests
import time
from pyquery import PyQuery as pq
# 异步

import gevent
import time
import gevent.monkey

gevent.monkey.patch_all()
"""
因为requests库在任何时候只允许有一个访问结束完全结束后，才能进行下一次访问。无法通过正规途径拓展成异步，
因此这里使用了monkey补丁
"""

def exeTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        print("@%s, {%s} 开始" % (time.strftime("%X", time.localtime()), func.__name__))
        back = func(*args, **args2)
        print("@%s, {%s} 结束" % (time.strftime("%X", time.localtime()), func.__name__))
        print("@%.3fs 异步编程 for {%s}" % (time.time() - t0, func.__name__))
        return back
    return newFunc

def get_data(url):
    html = requests.get(url).text
    for item in pq(html)('.item').items():
        title = item.find('.title').html()
        # #  <span class="title">肖申克的救赎</span><span class="title"> / The Shawshank Redemption</span>
        # #  返回第一个 .title里面的内容
        num = item.find('.pic em').text()
        star = item.find('.rating_num').text()
        img = item.find('.pic a img').attr('src')
        print(num, title, star, img)

@exeTime
def get_all(urls):
    events = [gevent.spawn(get_data, url) for url in urls]
    # spawn的意思是分支
    # 把大的任务分解成小任务

    gevent.joinall(events)
    # gevent.joinall 法会阻塞当前程序

if __name__ == '__main__':
    urls = ['https://movie.douban.com/top250?start=%s'%str(page_num) for page_num in range(0, 250 ,25)]
    get_all(urls)
    # @0.733s 异步taken for {get_all}


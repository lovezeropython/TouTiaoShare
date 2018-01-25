# -*- coding: utf-8 -*-
"""
@Time: 2018/1/24
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),])

import random

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)

#同步（结果更像串行）
def synchronous():
    for i in range(1,10):
        task(i)

#异步（结果更像乱步）
def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

print('Synchronous同步:')
synchronous()

print('Asynchronous异步:')
asynchronous()

import requests
from pyquery import PyQuery as pq
import gevent
import time
import gevent.monkey

gevent.monkey.patch_all()

"""
因为requests库在任何时候只允许有一个访问结束完全结束后，才能进行下一次访问。无法通过正规途径拓展成异步
，因此这里使用了monkey补丁
"""
def fetch_word_info(word):
    url = "http://dict.youdao.com/w/eng/{}/".format(word)

    resp = requests.get(url)
    doc = pq(resp.text)

    pros = ''
    for pro in doc.items('.baav .pronounce'):
        pros += pro.text()

    description = ''
    for li in doc.items('#phrsListTab .trans-container ul li'):
        description += li.text()

    return {'word': word, '音标': pros, '注释': description}


words = ['good', 'bad', 'cool',
         'hot', 'nice', 'better',
         'head', 'up', 'down',
         'right', 'left', 'east']


def synchronous():
    start = time.time()
    print('同步开始了')
    for word in words:
        print(fetch_word_info(word))
    end = time.time()
    print("同步运行时间： %s 秒" % str(end - start))


# 执行同步
synchronous()



import requests
from pyquery import PyQuery as pq
import gevent
import time
import gevent.monkey
gevent.monkey.patch_all()

words = ['good','bad','cool',
         'hot','nice','better',
         'head','up','down',
         'right','left','east']

def asynchronous():
    start = time.time()
    print('异步开始了')
    events = [gevent.spawn(fetch_word_info,word) for word in words]
    wordinfos = gevent.joinall(events)
    for wordinfo in wordinfos:
        #获取到数据get方法
        print(wordinfo.get())
    end = time.time()
    print("异步运行时间： %s 秒"%str(end-start))

#执行异步
asynchronous()

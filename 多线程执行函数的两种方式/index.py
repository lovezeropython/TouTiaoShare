# -*- coding: utf-8 -*-
"""
@Time: 2018/1/27
@Author: songhao
@微信公众号: zeropython
@File: index.py
"""
import threading,time
from time import sleep, ctime

# 返回当前时间的函数
def now() :
    return str(time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )

# 多线程传入的函数
def test(nloop, nsec):
    print('start loop', nloop, 'at:', now())
    sleep(nsec)
    print('loop', nloop, 'done at:', now())
# 主函数
def main():
    print('starting at:',now())
    threadpool=[]

    # 创建10个多线程
    for i in range(10):
        th = threading.Thread(target= test,args= (i,2))
        threadpool.append(th)
    # 开启多线程
    for th in threadpool:
        th.start()
    # 阻塞多线程
    for th in threadpool:
        threading.Thread.join(th)

    print('all Done at:', now())
if __name__ == '__main__':
    main()
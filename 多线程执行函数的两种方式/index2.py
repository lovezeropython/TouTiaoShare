# -*- coding: utf-8 -*-
"""
@Time: 2018/1/27
@Author: songhao
@微信公众号: zeropython
@File: index2.py
"""
# 导入多线程用到的类
import threading ,time
from time import sleep, ctime

def now() :
    return str( time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )

# 继承多线程的类
class myThread (threading.Thread) :
    """docstring for myThread"""
    def __init__(self, nloop, nsec) :
        super(myThread, self).__init__()
        self.nloop = nloop
        self.nsec = nsec
    #  多线程执行函数
    def run(self):
        print('start loop', self.nloop, 'at:', ctime())
        sleep(self.nsec)
        print('loop', self.nloop, 'done at:', ctime())

# 主函数
def main():
    thpool=[]
    print('starting at:',now())
    for i in range(10):
        thpool.append(myThread(i,2))
    for th in thpool:
        th.start()
    for th in thpool:
        th.join()
    print('all Done at:', now())
if __name__ == '__main__':
     main()
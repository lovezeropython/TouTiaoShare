# -*- coding: utf-8 -*-
"""
@Time: 2018/1/29
@Author: songhao
@微信公众号: zeropython
@File: read_big_file.py
@ website:https://www.168seo.cn/python/24379.html
"""


# 微信公众号: zeropython
# 大家如何方便可以点击下广告 谢谢

def read_in_chunks(file_object, chunk_size=1024):
    """把文件切割成一块块的读，默认大小是1024k"""
    while True:
        data = file_object.read(chunk_size)
        # 如果不存在存在data
        if not data:
            # 跳出
            break
        yield data


f = open('new.log')
for piece in read_in_chunks(f):
    # 对文件进行读写
    process_data(piece)
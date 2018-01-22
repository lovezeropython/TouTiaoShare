# -*- coding: utf-8 -*-
"""
@Time: 2018/1/16
@Author: songhao
@微信公众号: zeropython
@File: c1.py
"""
import os
from urllib.request import urlopen

import requests
from tqdm import tqdm


def download_from_url(url, dst):
    """
    @param: url to download file
    @param: dst place to put the file
    """
    # 获取文件的大小
    file_size = int(urlopen(url).info().get('Content-Length', -1))

    # 查看文件是否存在
    if os.path.exists(dst):
        # 如果存在获取文件的大小a
        first_byte = os.path.getsize(dst)
    else:
        # 如果不存在在 为0
        first_byte = 0

    if first_byte >= file_size:
        return file_size
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}

    pbar = tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=url.split('/')[-1])

    """
    initial : int, optional
    The initial counter value. Useful when restarting a progress
    bar [default: 0].
    初始计数器值，默认为0

    unit : str, optional
    String that will be used to define the unit of each iteration
    [default: it].
    将被用来定义每个单元的字符串？？？

    unit_scale : bool, optional
    If set, the number of iterations will be reduced/scaled
    automatically and a metric prefix following the
    International System of Units standard will be added
    (kilo, mega, etc.) [default: False].
    如果设置，迭代的次数会自动按照十、百、千来添加前缀，默认为false

    desc : str, optional
    Prefix for the progressbar.
    进度条的描述

    """
    req = requests.get(url, headers=header, stream=True)
    with(open(dst, 'ab')) as f:
        # 下载文件
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                # 更新文件大小
                pbar.update(1024)
    pbar.close()
    return file_size


if __name__ == '__main__':
    url = "http://newoss.maiziedu.com/machinelearning/pythonrm/pythonrm5.mp4"
    download_from_url(url, "./new.mp4")
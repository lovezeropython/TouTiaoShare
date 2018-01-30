# -*- coding: utf-8 -*-
"""
@Time: 2018/1/15
@Author: songhao
@微信公众号: zeropython
@File: spider.py
"""
# 导入工程中用到的库文件
import re, os
import requests,time
from hashlib import md5
from multiprocessing import Pool


def get_html(url):
    """
    :param url: url
    :return:  html源码
    """
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    return None

def get_list_href(html):
    """
    :param html: html源码
    :return: 返回列表页面的对应图片内容页的网址
    """
    req = '<div class="related-title"><h2><a href="(.*?)" class="related-item-link">'
    hrefs = re.findall(req, html, re.S)
    # print(hrefs)
    if hrefs:
        return hrefs
    return None

def get_image_url(ht):
    """
    :param ht: image_url 内页源码
    :return: 返回相对应的url
    """
    req = '<div class="display-image full">\s*<img class="center" draggable="false" src="(.*?)"'
    img_href = re.search(req, ht, re.S)
    if img_href:
        return img_href.group(1)
    return None


def save_image(img_url):
    '''
        format 字符串格式化
        os.getcwd() 获取当前的目录
        md5(content).hexdigest() 生成md5
        os.path.exists检测文件是否存在
    '''
    ir = requests.get(img_url)
    if ir.status_code == 200:
        content = ir.content
        file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
        print(file_path)
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(content)
                #二进制写入
    else:
        print("已存在")
    print("下载完成", img_url)


def main():

    first_url = "https://hdwallsource.com/?page=%d"
    # 构造url
    get_all_urls = [first_url%x for x in range(1,5)]
    all_imges = []
    for i in get_all_urls:
        ht = get_html(i)
        if ht:
            list_hrefs = get_list_href(ht)
            for list_href in list_hrefs:
                list_href_ht = get_html(list_href)
                imgurl = get_image_url(list_href_ht)
                print("put img url to all_imges", imgurl)
                all_imges.append(imgurl)
    # 创建 10个进程
    pool = Pool(processes=10)
    for imgurl in all_imges:
        print("开始下载", imgurl)
        pool.apply_async(save_image, args=(imgurl,))
        # save_image(imgurl)
    pool.close()
    pool.join()


if __name__ == '__main__':
    start = time.time()
    main()
    print('[info]耗时：%s' % (time.time() - start))

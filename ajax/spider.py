# -*- coding: utf-8 -*-
"""
@Time: 2018/1/24
@Author: songhao
@微信公众号: zeropython
@File: spider.py
"""
#-*- coding:utf-8 -*-
import requests
import json
import re
url = 'https://www.huxiu.com/chuangye/ajax_get_company_list_for_index'
data = {'huxiu_hash_code':'aafab17210f4ac94f6a6670ad6222783','page':2}
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

try:
    r = requests.post(url=url,data=data ,headers = headers)
    html = r.text
    # print(html)
    #解析json
    result = json.loads(html)
    print(result['msg'])
    data = result.get('data')
    # re 提取标题`
    content = re.findall('<h2 class="cy-cp-name">(.*?)</h2>',data,re.S)

    # 去除网站标题的空格换行
    content = [x.strip() for x in content]
    print(content)


except Exception as e:
     print(e)
    #这样子的话，大部分网页就能抓了，管他是post还是get。
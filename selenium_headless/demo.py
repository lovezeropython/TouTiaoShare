# -*- coding: utf-8 -*-
"""
@Time: 2018/1/29
@Author: songhao
@微信公众号: zeropython
@File: demo.py
"""
#coding:utf-8
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# 增加无界面选项
chrome_options.add_argument('--headless')
# 如果不加这个选项 有时候定位会出现问题,定位会偏左
chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/Users/xxxx/driver/chromedriver')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.168seo.cn')
print("当前标题",driver.title)
print("当前网址",driver.current_url)
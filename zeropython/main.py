# -*- coding: utf-8 -*-
"""
@Time: 2018/1/22
@Author: songhao
@微信公众号: zeropython
@File: main.py
"""
import scrapy
# 引入CrawlProcess
from scrapy.crawler import CrawlerProcess

# 爬虫1
class SeoSpider(scrapy.Spider):
    name = 'seo'
    allowed_domains = ['www.168seo.cn']
    start_urls = ['https://www.168seo.cn/']

    def parse(self, response):
        print(response.css('title::text').extract_first())

# 爬虫2
class Seo2Spider(scrapy.Spider):
    name = 'seo2'
    allowed_domains = ['www.168seo.cn']
    start_urls = ['https://www.168seo.cn/']

    def parse(self, response):
        print(response.css('title::text').extract_first())


process = CrawlerProcess()

process.crawl(SeoSpider)
process.crawl(Seo2Spider)
process.start()
# the script will block here until all crawling jobs are finished


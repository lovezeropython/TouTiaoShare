# -*- coding: utf-8 -*-
"""
@Time: 2018/1/22
@Author: songhao
@微信公众号: zeropython
@File: main.py
"""
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

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


configure_logging()
runner = CrawlerRunner()
runner.crawl(SeoSpider)
runner.crawl(Seo2Spider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run() # the script will block here until all crawling jobs are finished
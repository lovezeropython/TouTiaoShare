# -*- coding: utf-8 -*-
import scrapy


class Seo2Spider(scrapy.Spider):
    name = 'seo2'
    allowed_domains = ['www.168seo.cn']
    start_urls = ['http://www.168seo.cn/']

    def parse(self, response):
        print(response.css('title::text').extract_first())

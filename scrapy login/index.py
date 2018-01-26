# -*- coding: utf-8 -*-
"""
@Time: 2018/1/26
@Author: songhao
@微信公众号: zeropython
@File: index.py
@ website:https://www.168seo.cn/python/1912.html
"""
from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule

class MySpider(InitSpider):
    name = 'myspider'
    allowed_domains = ['domain.com']
    login_page = 'http://www.domain.com/login'
    start_urls = ['http://www.domain.com/useful_page/',
                  'http://www.domain.com/another_useful_page/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
             callback='parse_item', follow=True),
    )

    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'name': 'herman', 'password': 'password'},
                    callback=self.check_login_response)

    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "Hi Herman" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            self.initialized()
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.

    def parse_item(self, response):
        # Scrape data from page
        pass


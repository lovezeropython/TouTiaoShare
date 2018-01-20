# -*- coding: utf-8 -*-

"""
@Time: 2018/1/18
@Author: songhao
@微信公众号: zeropython
@File: superclass.py
@website:https://www.168seo.cn/python/24344.html
"""
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
# 本模块定义标准Python 编码解码器（编码器和解码器）的基类
import json

from scrapy.pipelines.images import ImagesPipeline
# scrapy 自带的图片处理的类
from scrapy.exporters import JsonItemExporter
# scrapy 导出json类 JsonItemExporter

import pymysql
import pymysql.cursors
# 导入pymysql 数据包

import pymongo
# 导入 Pymongo

from twisted.enterprise import adbapi

"""
Twisted 是一个异步网络框架，不幸的是大部分数据库api实现只有阻塞式接口，
twisted.enterprise.adbapi为此产生，它是DB-API 2.0 API的非阻塞接口，可以访问各种关系数据库
"""


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        # 打开文件
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        # 写入文件
        return item
        # 一定要return item，因为后边的piplines要处理

    def spider_closed(self, spider):
        self.file.close()
        # 关闭文件


class MysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        self.conn = pymysql.connect('192.168.0.106', 'root', 'root', 'article', charset="utf8", use_unicode=True)
        # 链接MySQL 数据库
        self.cursor = self.conn.cursor()

    # 获取MySQL 数据库指针
    def process_item(self, item, spider):
        insert_sql = """
            insert into article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))
        # 执行 导入数据
        self.conn.commit()
    # 提交数据


class MysqlTwistedPipline(object):
    """
    异步存储数据
    非阻塞型
    """
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)
    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常
    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)
    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        print(insert_sql, params)
        cursor.execute(insert_sql, params)


class JsonExporterPipleline(object):
    # 调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        # 打开文件
        self.exporter.start_exporting()

    # 导出文件

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    #  文件关闭

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MongoPipeline(object):
    # mongodb 数据库存储
    collection_name = 'scrapy_items'
    # 数据库名称
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    @classmethod
    def from_crawler(cls, crawler):
        # 从settings 获取 MONGO_URI，MONGO_DATABASE
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )
    def open_spider(self, spider):
        # 数据库打开配置
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    def close_spider(self, spider):
        # 数据库关闭
        self.client.close()
    def process_item(self, item, spider):
        # 数据库储存
        self.db[self.collection_name].insert_one(dict(item))
        return item
        # 切记 一定要返回item进行后续的pipelines 数据处理

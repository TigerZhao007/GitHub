# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DoubanItem(scrapy.Item):
    serial_number = scrapy.Field()    # 序号
    movie_name = scrapy.Field()    # 电影名称
    introduce = scrapy.Field()    # 简介
    star = scrapy.Field()    # 明星
    evaluate = scrapy.Field()    # 评价
    describtion = scrapy.Field()    # 描述

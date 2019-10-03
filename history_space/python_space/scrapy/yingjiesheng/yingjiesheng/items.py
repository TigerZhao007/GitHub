# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YingjieshengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    company = scrapy.Field()
    school = scrapy.Field()
    area = scrapy.Field()
    city_link = scrapy.Field()
    company_link = scrapy.Field()
    school_link = scrapy.Field()
    detail_link = scrapy.Field()

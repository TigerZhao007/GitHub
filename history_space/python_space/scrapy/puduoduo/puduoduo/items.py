# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PuduoduoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    xinxibiaoti = scrapy.Field()
    xinxilaiyuan = scrapy.Field()
    suozaidiqu = scrapy.Field()
    shangpuleixing = scrapy.Field()
    shangpumianji = scrapy.Field()
    shangpuzujin = scrapy.Field()
    lianxiren = scrapy.Field()
    zhuanrangfeiyong = scrapy.Field()
    shiyingjingying = scrapy.Field()
    xiangxidizhi = scrapy.Field()
    fabushijian = scrapy.Field()
    liulancishu = scrapy.Field()
    xiangxixinxi = scrapy.Field()
    fangyuantupian = scrapy.Field()


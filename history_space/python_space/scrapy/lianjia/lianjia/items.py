# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题部分
    title = scrapy.Field()          # 'title': '标题'
    jianjie = scrapy.Field()        #'jianjie': '简介',
    guanzhurenshu = scrapy.Field()  #'guanzhunum': '关注人数',
    shoucangrenshu = scrapy.Field() # 'shoucangnum': '收藏人数',
    link = scrapy.Field()           # 'link': '网页链接',

    # 售房信息部分
    totleprice = scrapy.Field()     #'totleprice': '总价',
    meanprice = scrapy.Field()      #'meanprice': '单价',
    taxprice = scrapy.Field()       #'taxprice': '税价',
    houseData = scrapy.Field()      #'houseDate': '建成年代',
    xiaoquname = scrapy.Field()     #xiaoquname': '小区名称',
    suozaiarea = scrapy.Field()     #suozaiarea': '所在区域',
    kanfangdata = scrapy.Field()    #'kanfangdata': '看房时间',
    lianjiabianhao = scrapy.Field() #'lianjiabianhao': '链家编号',

    # 基本属性部分
    fangwuhuxing = scrapy.Field()   #'fangwuhuxing': '房屋户型',
    houseFloor = scrapy.Field()     #'houseFloor': '所在楼层',
    jianzhumianji = scrapy.Field()  #'jianzhumianji': '建筑面积',
    huxingjiegou = scrapy.Field()   #'huxingjiegou': '户型结构',
    taoneimianji = scrapy.Field()   #'taoneimianji': '套内面积',
    buildingType = scrapy.Field()   #'buildingType': '建筑类型',
    houseOrientation = scrapy.Field()  #'houseOrientation': '房屋朝向',
    jianzhujiegou = scrapy.Field()  #'jianzhujiegou': '建筑结构',
    Decoration = scrapy.Field()     #'Decoration': '装修情况',
    tihubili = scrapy.Field()       #'tihubili': '梯户比例',
    ladder = scrapy.Field()         #'ladder': '配备电梯',
    chanquannianxian = scrapy.Field()  #'chanquannianxian': '产权年限',
#    gongnuanfangshi = scrapy.Field()   #'gongnuanfangshi': '供暖方式',

    # 交易属性部分
    gaipaidata = scrapy.Field()     #'gaipaidata': '挂牌时间',
    jiaoyidata = scrapy.Field()     #'jiaoyidata': '交易时间',
    lastjiaoyidata = scrapy.Field() #'lastjiaoyidata': '上次交易',
    fangwuyongtu = scrapy.Field()   #'fangwuyongtu': '房屋用途',
    fangwunianxian = scrapy.Field() #'fangwunianxian': '房屋年限',
    chanquansuoshu = scrapy.Field() #'chanquansuoshu': '产权所属',
    diyaxinxi = scrapy.Field()      #'diyaxinxi': '抵押信息',
    fangbenbeijian = scrapy.Field() #'fangbenbeijian': '房本备件',

    # 房源特色部分
    fangyuantese = scrapy.Field()   # 'fangyuantese': '房源特色',

    # h户型分间部分
    huxingfenjian = scrapy.Field()  #'huxingfenjian': '户型分间'


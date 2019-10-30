# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import pymysql
import csv

class PuduoduoPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1',
                               user = 'root',
                               password = 's3438838',
                               db = 'webdata',
                               charset="utf8")
        cur = conn.cursor()

        # 创建数据库
        sql1 = """CREATE TABLE IF NOT EXISTS puduoduo(
                xinxibiaoti text,xinxilaiyuan text,suozaidiqu text,shangpuleixing text,shangpumianji text,
                shangpuzujin text,lianxiren text,zhuanrangfeiyong text,shiyingjingying text,xiangxidizhi text,
                fabushijian text,liulancishu text,xiangxixinxi text,link text,fangyuantupian text)
                 """
        cur.execute(sql1)

        # 上传数据库
        sql2 = """INSERT INTO puduoduo(
        xinxibiaoti ,xinxilaiyuan ,suozaidiqu ,shangpuleixing ,shangpumianji ,
        shangpuzujin ,lianxiren ,zhuanrangfeiyong ,shiyingjingying ,xiangxidizhi ,
        fabushijian ,liulancishu ,xiangxixinxi, link ,fangyuantupian 
        ) value
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        lis = (item['xinxibiaoti'], item['xinxilaiyuan'], item['suozaidiqu'], item['shangpuleixing'],
               item['shangpumianji'], item['shangpuzujin'], item['lianxiren'], item['zhuanrangfeiyong'],
               item['shiyingjingying'], item['xiangxidizhi'], item['fabushijian'], item['liulancishu'],
               item['xiangxixinxi'], item['link'], item['fangyuantupian'])

        cur.execute(sql2, lis)
        print('成功保存%s房屋信息'%(item['link']))
        conn.commit()

        cur.close()
        conn.close()

        return item


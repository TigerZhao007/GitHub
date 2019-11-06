# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import pymysql
import csv

class MeizituPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1',
                               user = 'root',
                               password = 's3438838',
                               db = 'personal',
                               charset="utf8")
        cur = conn.cursor()

        # 创建数据库
        sql1 = """CREATE TABLE IF NOT EXISTS meizitu1(
                name text,link text,data text,date text)
                 """

        cur.execute(sql1)

        # 上传数据库
        sql2 = """INSERT INTO meizitu1(
        name,link,data,date
        ) value
        (%s,%s,%s,%s)"""
        lis = (item['name'],item['link'],item['data'], item['date'])

        cur.execute(sql2, lis)
        print('成功保存%s'%(item['name']))
        conn.commit()

        cur.close()
        conn.close()

        return item

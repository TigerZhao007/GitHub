# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql.cursors
import pymysql

class DoubanPipeline(object):
    # douban_item为spider传递过来的名字。
    def process_item(self, douban_item, spider):
        # 链接数据库
        conn = pymysql.connect(host='127.0.0.1',
                               user = 'root',
                               password = 's3438838',
                               db = 'webdata',
                               charset="utf8")
        cur = conn.cursor()

        # 创建数据库代码
        sql1 = """CREATE TABLE IF NOT EXISTS douban_top250(
                serial_number text, movie_name text,
                star text,     introduce text,
                evaluate text, describtion text)
                 """
        # 执行创建数据库
        cur.execute(sql1)

        # 上传数据库代码
        sql2 = """INSERT INTO douban_top250(serial_number,movie_name,star,introduce,evaluate,describtion) value
        (%s,%s,%s,%s,%s,%s)"""
        # 上次数据库数据
        lis = (douban_item['serial_number'],douban_item['movie_name'],douban_item['star'],douban_item['introduce'],
               douban_item['evaluate'], douban_item['describtion'])
        # 执行上传数据库
        cur.execute(sql2, lis)

        # 打印保存数据进度
        print('成功保存编号%s房源'%(douban_item['serial_number']))
        # 提交数据
        conn.commit()

        # 关闭数据库链接
        cur.close()
        conn.close()

        return douban_item
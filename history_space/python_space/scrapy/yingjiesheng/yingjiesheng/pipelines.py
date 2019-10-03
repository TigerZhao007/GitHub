# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import pymysql
class YingjieshengPipeline(object):
    def process_item(self, xjh_item, spider):
        # 链接数据库
        # print('????????')
        conn = pymysql.connect(host='127.0.0.1',
                               user = 'root',
                               password = 's3438838',
                               db = 'webdata',
                               charset="utf8")
        cur = conn.cursor()

        # 创建数据库代码
        sql1 = """CREATE TABLE IF NOT EXISTS yingjieshengxjh(
                city text,     date text,
                time text,     company text,
                school text,   area text,
                city_link text,   company_link text,
                school_link text, detail_link text)
                 """
        # 执行创建数据库
        cur.execute(sql1)

        # 上传数据库代码
        sql2 = """INSERT INTO yingjieshengxjh(city,date,time,company,
        school,area,city_link,company_link,school_link,detail_link) value
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # 上次数据库数据
        lis = (xjh_item['city'], xjh_item['date'], xjh_item['time'], xjh_item['company'],
               xjh_item['school'], xjh_item['area'], xjh_item['city_link'], xjh_item['company_link'],
               xjh_item['school_link'], xjh_item['detail_link'])
        # 执行上传数据库
        cur.execute(sql2, lis)

        # 打印保存数据进度
        print('成功保存编号%s宣讲会'%(xjh_item['company']))
        # 提交数据
        conn.commit()

        # 关闭数据库链接
        cur.close()
        conn.close()

        return xjh_item

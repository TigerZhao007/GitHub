# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import pymysql
import csv

class LianjiaPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1',
                               user = 'root',
                               password = 's3438838',
                               db = 'webdata',
                               charset="utf8")
        cur = conn.cursor()

        # 创建数据库
        sql1 = """CREATE TABLE IF NOT EXISTS lianjia_ershoufang(
                title text,jianjie text,
                guanzhurenshu text,shoucangrenshu text,link text,                
                totleprice text,meanprice text,
                taxprice text,houseData text,
                xiaoquname text,suozaiarea text,
                kanfangdata text,lianjiabianhao text,                
                fangwuhuxing text,houseFloor text,
                jianzhumianji text,huxingjiegou text,
                taoneimianji text,buildingType text,
                houseOrientation text,jianzhujiegou text,
                Decoration text,tihubili text,
                ladder text,chanquannianxian text,                
                gaipaidata text,jiaoyidata text,
                lastjiaoyidata text,fangwuyongtu text,
                fangwunianxian text,chanquansuoshu text,
                diyaxinxi text,fangbenbeijian text,                
                fangyuantese text,huxingfenjian text)
                 """

        cur.execute(sql1)

        # 上传数据库
        sql2 = """INSERT INTO lianjia_ershoufang(title,jianjie,guanzhurenshu,shoucangrenshu,link,
                                    totleprice,meanprice,taxprice,houseData,
                                    xiaoquname,suozaiarea,kanfangdata,lianjiabianhao,
                                    fangwuhuxing,houseFloor,jianzhumianji,huxingjiegou,
                                    taoneimianji,buildingType,houseOrientation,jianzhujiegou,
                                    Decoration,tihubili,ladder,chanquannianxian,
                                    gaipaidata,jiaoyidata,lastjiaoyidata,fangwuyongtu,
                                    fangwunianxian,chanquansuoshu,diyaxinxi,fangbenbeijian,
                                    fangyuantese,huxingfenjian) value
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        lis = (item['title'],item['jianjie'],item['guanzhurenshu'],item['shoucangrenshu'],item['link'],
               item['totleprice'], item['meanprice'], item['taxprice'], item['houseData'],
               item['xiaoquname'], item['suozaiarea'], item['kanfangdata'], item['lianjiabianhao'],
               item['fangwuhuxing'],item['houseFloor'],item['jianzhumianji'],item['huxingjiegou'],
               item['taoneimianji'],item['buildingType'],item['houseOrientation'],item['jianzhujiegou'],
               item['Decoration'],item['tihubili'],item['ladder'],item['chanquannianxian'],
               item['gaipaidata'],item['jiaoyidata'],item['lastjiaoyidata'],item['fangwuyongtu'],
               item['fangwunianxian'],item['chanquansuoshu'],item['diyaxinxi'],item['fangbenbeijian'],
               item['fangyuantese'],item['huxingfenjian'])

        cur.execute(sql2, lis)
        print('成功保存编号%s房源'%(item['lianjiabianhao']))
        conn.commit()

        cur.close()
        conn.close()

        return item


# ############################
# import json
# person_action = open()
import pymongo
import pandas as pd
from bson.objectid import ObjectId
import pickle
import pandas as pd

# ############################
# 建立连接
client = pymongo.MongoClient("localhost", 27017) # 服务器

# 指定数据库
db = client.testdb

# 指定集合
collection = db.test_student

# ############################
# 指定要查询的内容（查询）
uid01 =  collection.find_one({'uid':'53242101'})
uid01["timeline"]
dic_test=[]
for item in uid01["timeline"]:
    item['detailInfo']['time']=item['time']
    item['detailInfo']['behavior']=item['behavior']
    dic_test.append(item['detailInfo'])

df = pd.DataFrame(dic_test)
df = df.sort_index(by='time')
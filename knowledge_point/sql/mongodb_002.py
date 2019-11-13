
# ############################
# 导入模块
# ############################
import pymongo
import pandas as pd
from bson.objectid import ObjectId

# ############################
# 待插入数据准备
# ############################
# 数据集1
# student1 = { "id" : 1, "name" : "小然", "gender" : 1, "age" : 22, "score" : 95 }
# student2 = { "id" : 2, "name" : "小红", "gender" : 0, "age" : 18, "score" : 80 }
# student3 = { "id" : 3, "name" : "小亮", "gender" : 1, "age" : 19, "score" : 60 }
# student4 = { "id" : 4, "name" : "小强", "gender" : 1, "age" : 23, "score" : 70 }
# student5 = { "id" : 5, "name" : "小柔", "gender" : 0, "age" : 20, "score" : 85 }
# student6 = { "id" : 6, "name" : "小雷", "gender" : 1, "age" : 25, "score" : 65 }
# student7 = { "id" : 7, "name" : "小冉", "gender" : 0, "age" : 19, "score" : 70 }
# student8 = { "id" : 8, "name" : "小晴", "gender" : 0, "age" : 18, "score" : 90 }
# student9 = { "id" : 9, "name" : "小齐", "gender" : 1, "age" : 24, "score" : 50 }

# ############################
# 建立连接
# ############################
client = pymongo.MongoClient("106.12.30.122", 32937) # 服务器

# ############################
# 指定数据库
# ############################
db = client.testdb

# ############################
# 指定集合,没有则自行创建
# ############################
collection = db.test_student02

# ############################
# 插入数据
# ############################
# 插入多条数据
# result2 = collection.insert_many([student1,student2,student3,student4,student5,student6,student7])

# ############################
# 指定要查询的内容（查询）
# ############################
# 查询多条数据
for result in collection.find():
    print(result)

# ############################
# 统计分析-聚合计算
# ############################
#
# db.test_student02.aggregate([{'$group':{'_id':"$gender", 'count': {'$sum': 1}}}])

db.test_student02.aggregate(
    { '$project' : { 'name' : 1 , 'gender' : 1 }}
 )




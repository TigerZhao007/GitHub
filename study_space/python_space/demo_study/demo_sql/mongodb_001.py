
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
student1 = {
    'id': '201807',
    'name': 'Jack',
    'age': 18,
    'gender': 'male'
}
student2 = {
    'id': '201808',
    'name': 'Tom',
    'age': 13,
    'gender': 'male'
}
student3 = {
    'id': '201809',
    'name': 'Rose',
    'age': 21,
    'gender': 'female'
}
student4 = {
    'id': '201810',
    'name': 'Mike',
    'age': 10,
    'gender': 'female'
}
student5 = {
    'id': '201811',
    'name': 'Ray',
    'age': 26,
    'gender': 'female'
}
student6 = {
    'id': '201812',
    'name': 'Alan',
    'age': 29,
    'gender': 'male'
}

# ############################
# 建立连接
# ############################
client = pymongo.MongoClient("localhost", 32937) # 服务器

# ############################
# 指定数据库
db = client.testdb
# ############################

# ############################
# 指定集合
# ############################
collection = db.test_student

# ############################
# 数据库、集合的创建、删除
# ############################
# 数据库的删除
# db.dropDatabase()
# 集合的创建
# db.createCollection(name, options)
# db.createCollection("sub") #???
# 集合的删除
# db.集合名称.drop()
# collection.remove({'name': 'Kevin'})
# collection.delete_one({'name': 'Kevin'})
# collection.delete_many({'age': {'$lt': 25}})

# ############################
# 插入数据
# ############################
# 插入一条数据
# result1 = collection.insert_one(student1)
# 插入多条数据
# result2 = collection.insert_many([student1,student2,student3,student4,student5,student6])
# print(result2.inserted_ids)

# ############################
# 更新数据
# ############################
# 方法一：update()方法（不推荐）
# condition = {'id': '201802'}
# student = collection.find_one(condition)
# student['age'] = 22
# result = collection.update(condition, student)
# print(result)
# 方法二：$set操作符（不推荐）
# result = collection.update(condition, {'$set': student})
# 方法三：分为update_one()方法和update_many()方法（推荐）

# ############################
# 指定要查询的内容（查询）
# ############################
# 查询一条数据find_one
collection.find_one({'id':'201801'})
# 查询多条数据find
results = collection.find({'age':{'$gt':20}})
for result in results:
    print(result)

# ############################
# 给定数值型条件查询（数字条件查询）
# ############################
for result in collection.find({'age':20}):   # 查询年龄 =20 的所有集合
    print(result)
for result in collection.find({'age':{'$lt':20}}):   # 查询年龄 <20 的所有集合
    print(result)
for result in collection.find({'age':{'$gt':20}}):   # 查询年龄 >20 的所有集合
    print(result)
for result in collection.find({'age':{'$lte':20}}):   # 查询年龄 <=20 的所有集合
    print(result)
for result in collection.find({'age':{'$gte':20}}):   # 查询年龄 >=20 的所有集合
    print(result)
for result in collection.find({'age':{'$ne':20}}):   # 查询年龄 !=20 的所有集合
    print(result)
for result in collection.find({'age':{'$in':[20,23]}}):   # 查询年龄 在【20,23】范围内 的所有集合，非区间（21不是）
    print(result)
for result in collection.find({'age':{'$nin':[20,23]}}):   # 查询年龄 不在【20,23】范围内 的所有集合，非区间（21不是）
    print(result)
for result in collection.find({'age':{'$mod':[5,0]}}):   # 数字模操作$mod，匹配任意年龄模5余0
    print(result)

# ############################
# 给定文本型条件查询（文本条件查询）
# ############################
for result in collection.find({'age':{'$regex':'^2.*'}}):   # 正则匹配regex，不适用与数值型数据。
    print(result)
for result in collection.find({'name':{'$regex':'^R.*'}}):   # 正则匹配regex，匹配任意以’R'开头的正则表达式。
    print(result)
for result in collection.find({'name':{'$exists':True}}):   # 属性是否存在exists，匹配任意name属性存在的集合
    print(result)
for result in collection.find({'age':{'$type':'int'}}):   # 类型判断$type，匹配任意age的类型为int
    print(result)
# for result in collection.find({'$text':  {'$search':'Mike'}}):   # 类型判断$type，匹配任意age的类型为int
#     print(result) # 报错？？？？？？？？？？？？？
for result in collection.find({'$where':'obj.name == "Mike"'}):   # 类型判断$type，匹配任意age的类型为int
    print(result)
for result in collection.find({'$where':'obj.age == 10'}):   # 类型判断$type，匹配任意age的类型为int
    print(result)
for result in collection.find({'age':{'$gt':20},'gender':'male'}):  # 多条件查询，
    print(result)

# ############################
# 逻辑判断（and/or）
# ############################
for result in collection.find({'$or':[{'name': "Mike"},{'age':10}]}):   # OR:
    print(result)
for result in collection.find({'name':{'$all':['Mike','Mik']}}):        # AND
    print(result)

# ############################
# 数据统计（计数）
# ############################
# 数据统计 - 计数
collection.find().count() # 统计集合总个数
collection.find({'id':'201801'}).count() # 统计编码为201801的集合个数
collection.find({'gender':'male'}).count() # 统计性别为男性的集合个数
collection.find({'age':{'$gt':20}}).count()  # 统计年龄大于20的集合个数
collection.count({'age':{'$gt':20},'gender':'male'})  # 统计年龄大于20，性别为男性的个数

# ############################
# 数据处理（去重、排序、偏移）
# ############################
collection.distinct('gender',{'age':{'$gt':20}})     # 去重，得到年龄大于20的性别字段的非重复值
for result in collection.find().sort('age', pymongo.ASCENDING):  # 排序：按照单个字段排序
    print(result)            # pymongo.DESCENDING为升序，pymongo.ASCENDING为降序
for result in collection.find().sort('age', pymongo.ASCENDING).skip(2):  # 偏移，忽略前两个集合
    print(result)
# 最好少用，可能会导致内存溢出，采用from bson.objectid import ObjectId
# collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})
for result in collection.find().sort('age', pymongo.ASCENDING).limit(2):  # limit，取前两个集合
    print(result)

# ############################
# 获取返回的值
# ############################
group_id = result['id']



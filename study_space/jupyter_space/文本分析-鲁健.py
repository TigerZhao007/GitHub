# -*- coding: utf-8 -*-
"""
Created on 2019/08/27
@author: jlu
application: text classification
"""

import pandas as pd
import sqlalchemy
import re
import datetime
import sys
import tqdm
import jieba
import jieba.analyse
from sklearn import svm
from sklearn import neighbors
import numpy as np
import matplotlib.pyplot as plt

# 数据库连接 ----------------------------------
wydb = sqlalchemy.create_engine(
    'postgresql://postgres:123456@localhost/wydb',
    pool_size=20, max_overflow=0
)
# 数据加载 ------------------------------------
with wydb.connect() as conn:
    wy_df = pd.read_sql_query('select * from "pre_rawdata_unproc_com"', conn)
wy_df.info()  # 数据基础信息
# wy_df.columns  # 数据列名
wy_df['reason_type_5th'].value_counts()  # 目标分类

# # 分词与TF-IDF测试
jieba.lcut(wy_df['content'][2], HMM=True)
jieba.analyse.extract_tags(wy_df['content'][0], topK=10, withWeight=True, allowPOS=())

# 数据预处理 ----------------------------------
# 截取2019年1-3月45747条数据
wy_df['year'].value_counts()  # 年份摘取
wy_df = wy_df[wy_df['year'] == 2019]
wy_df['month'].value_counts()  # 月份摘取
wy_df = wy_df[wy_df['month'].isin([1, 2, 3])]
wy_df = wy_df[wy_df['content'].notnull()]
wy_df = wy_df[wy_df['reason_type_5th'].notnull()]
wy_df = wy_df[wy_df['reason_type_5th'] != '（停车）停车收费问题']
wy_df = wy_df[wy_df['reason_type_5th'] != '（道路）路灯设施破损、被盗、新建']
wy_df = wy_df.reset_index()  # 重置索引
# wy_df = wy_df.iloc[:2000, :]  # 只取2000条
# 删去诉求内容中地址信息: 地址信息TF-IDF值较高，对目标是干扰信息
start_time = datetime.datetime.now()
for row_id in range(len(wy_df)):
    if wy_df.loc[row_id, 'address']:
        temp_address = re.escape(wy_df.loc[row_id, 'address'])  # 地址字符串转义
        wy_df.loc[row_id, 'content_test'] = re.sub(temp_address+'|[a-z0-9]', '', wy_df.loc[row_id, 'content'], re.I)
end_time = datetime.datetime.now()
print(end_time-start_time)  # 2分51秒

# TF-IDF测试
# jieba.analyse.extract_tags(wy_df['content_test'][0], topK=10, withWeight=True, allowPOS=())

# 普通分词统计 -----------------------------------------
simple_list = list()
for i in range(len(wy_df)):
    simple_list.extend(jieba.lcut(wy_df['content_test'][i], HMM=True))
print(pd.Series(simple_list).value_counts()[:30])
# TF-IDF统计 ---------------------------------------------
tfidf_list = list()
for j in range(len(wy_df)):
    tfidf_list.extend(jieba.analyse.extract_tags(wy_df['content_test'][j], topK=10, withWeight=False, allowPOS=()))
print(pd.Series(tfidf_list).value_counts()[:50])
# TF-IDF分类统计 ----------------------------------------
tfidf_df = pd.DataFrame()
for category in wy_df['reason_type_5th'].value_counts().index.tolist():
    temp_df = wy_df[wy_df['reason_type_5th'] == category]
    temp_df = temp_df.reset_index()  # 重置索引
    temp_list = list()
    for j in range(len(temp_df)):
        temp_list.extend(jieba.analyse.extract_tags(temp_df['content_test'][j], topK=10, withWeight=False, allowPOS=()))
    temp_series = pd.Series(pd.Series(temp_list).value_counts()[:25].index)
    tfidf_df[category] = temp_series

# 目标数据框
# target_string = '\n'.join(wy_df['content_test'])
# 四万*一万矩阵
# test_df = pd.DataFrame(columns=set(tfidf_list), index=range(len(wy_df)))
# sys.getsizeof(test_df)/1024/1024
# for j in range(len(wy_df)):
#     test_list = jieba.analyse.extract_tags(wy_df['content_test'][j], topK=10, withWeight=False, allowPOS=())
#     test_df.loc[j, test_list] = 1

# 2000*120矩阵
test_df = pd.DataFrame(columns=set(sum(tfidf_df.values.tolist(), [])), index=range(len(wy_df)))
sys.getsizeof(test_df)/1024/1024
for j in range(len(wy_df)):
    test_list = [x for x in set(sum(tfidf_df.values.tolist(), [])) if x in wy_df.loc[j, 'content_test']]
    test_df.loc[j, test_list] = 1
    if j % 200 == 0:
        print(j)
test_df = test_df.where(test_df.notnull(), 0)
test_df['classify'] = wy_df['reason_type_5th']

# test_df.to_excel('C:/Users/yikdata/Desktop/test_df.xlsx', index=False)
test_df = pd.read_excel('C:/Users/yikdata/Desktop/test_df.xlsx', index_col=False)
test_df = test_df[test_df['classify'].notnull()]
test_df = test_df.reset_index()
test_df['classify'].value_counts()

# SVM ----------------------------------------------
type_cover = {'（小区）物业服务、收费': 0, '（小区）小区出新工程': 1,
              '（小区、停车）小区内车位、停车问题': 2, '（小区）物业设施使用、维护': 3,
              '（小区）小区内垃圾、环境、绿化': 4, '（小区）小区内群租房问题': 5,
              '（小区）小区内路灯、楼道灯维护': 6, '（停车）地锁、停车桩问题': 7}
# for j in range(len(test_df)):
#     test_df['classify'][j] = type_cover[test_df['classify'][j]]
test_df['classify'] = [type_cover[x] for x in test_df['classify']]
model = svm.SVC(kernel='linear')
model.fit(test_df.iloc[:, :2].values.tolist(), test_df['classify'].values.tolist())
model.score(test_df.iloc[:, :2], test_df['classify'])

# KNN -------------------------------------------------
# neighbors.NearestNeighbors(n_neighbors=20, algorithm='ball_tree').fit(test_df.iloc[:, :119], test_df['classify'])

X = test_df.iloc[:, :2].values
y = test_df['classify'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)
from sklearn.neighbors import KNeighborsClassifier

neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

for i, k in enumerate(neighbors):
    # Setup a knn classifier with k neighbors
    knn = KNeighborsClassifier(n_neighbors=k)
    # Fit the model
    knn.fit(X_train, y_train)
    # Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)
    # Compute accuracy on the test set
    test_accuracy[i] = knn.score(X_test, y_test)

plt.title('k-NN Varying number of neighbors')
plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
plt.plot(neighbors, train_accuracy, label='Training accuracy')
plt.legend()
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')
plt.show()

knn = neighbors.KNeighborsClassifier(n_neighbors=20)
knn.fit(test_df.iloc[:, :119], test_df['classify'])
from sklearn.metrics import confusion_matrix
y_pred = knn.predict(test_df.iloc[:, :119])
confusion_matrix(test_df['classify'], y_pred)
pd.crosstab(test_df['classify'], y_pred, rownames=['True'], colnames=['Predicted'], margins=True)


# 分类合理性测试 -------------------------------------
category_df = pd.DataFrame(index=tfidf_df.columns, columns=tfidf_df.columns)
for i in category_df.columns:
    for j in category_df.index:
        score = 0
        for temp_string in wy_df[wy_df['reason_type_5th'] == j]['content_test']:
            if any([x in temp_string for x in tfidf_df[i]]):
                score = score+1
        category_df.loc[j, i] = round(score/len(wy_df[wy_df['reason_type_5th'] == j]), 4)

category_df.to_excel('C:/Users/yikdata/Desktop/category_df.xlsx', index=True)

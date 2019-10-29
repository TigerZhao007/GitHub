# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：算法基础-python自带数据集。
"""

# ######################################################################################################################
# 鸢尾花数据集，数据介绍
# ######################################################################################################################
from sklearn.datasets import load_iris
import pandas as pd

# 加载鸢尾花数据集
iris = load_iris()

x = iris.data                                  # x为数据集的属性集
y = iris.target                                # y为数据集的类别集（标签）
test = x[1:3]

# ######################################################################################################################
# 常用机器学习模型
# https://blog.csdn.net/roger_royer/article/details/79062482
# https://blog.csdn.net/weixin_33738555/article/details/86358096
# ######################################################################################################################

# 线性回归~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.linear_model import LinearRegression
module = LinearRegression()
module.fit(x, y)
module.score(x, y)
module.predict(test)

# 逻辑回归~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.linear_model import LogisticRegression
module = LogisticRegression()
module.fit(x, y)
module.score(x, y)
module.predict(test)

# K近邻~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
module = KNeighborsClassifier(n_neighbors=6)
module.fit(x, y)
predicted = module.predict(test)
predicted = module.predict_proba(test)

# 支持向量机~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn import svm
module = svm.SVC(probability=True)
module.fit(x, y)
module.score(x, y)
module.predict(test)
module.predict_proba(test)

# 朴素贝叶斯分类器~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.naive_bayes import GaussianNB
module = GaussianNB()
module.fit(x, y)
predicted = module.predict(test)

# 决策树分类器~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn import tree
module = tree.DecisionTreeClassifier(criterion='gini')
module.fit(x, y)
module.score(x, y)
module.predict(test)

# kmeans聚类~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.cluster import KMeans
module = KMeans(n_clusters=3, random_state=0)
module.fit(x, y)
module.predict(test)

# 随机森林~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
module = RandomForestClassifier()
module.fit(x, y)
module.predict(test)

# Gradient Boosting 和 AdaBoost算法~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
module = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=1, random_state=0)
module.fit(x, y)
module.predict(test)

# PCA特征降维~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn.decomposition import PCA
pca = PCA(n_components=2, svd_solver='full')
# pca.fit(x)
train_reduced = pca.fit_transform(x)
test_reduced = pca.transform(test)

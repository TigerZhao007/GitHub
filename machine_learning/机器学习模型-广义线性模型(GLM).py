# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：机器学习模型-广义线性模型(Generalized Linear Models)（普通最小二乘法）
"""

# ######################################################################################################################
# 鸢尾花数据集，数据介绍
# ######################################################################################################################
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# 加载 diabetes 数据集
diabetes = datasets.load_diabetes()

# 仅使用第一个特征
diabetes_X = diabetes.data[:, np.newaxis, 2]

# 把数据划分成训练集和测试集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# 把目标值划分成对应的训练集和测试集
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# ######################################################################################################################
# 机器学习模型-广义线性模型(Generalized Linear Models)（普通最小二乘法）
# ######################################################################################################################

# 线性回归（普通最小二乘法）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn import linear_model  # 导入线性回归模块

# 广义线性模型实现~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 实例化一个 线性回归 类的对象
regr = linear_model.LinearRegression()

# 在训练集上训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

# 回归模型参数查看~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
regr.coef_         # 查看变量的系数
regr.intercept_    # 查看截矩项

# 在测试集上进行预测~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
diabetes_y_pred = regr.predict(diabetes_X_test)

# 模型效果检验~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 均方误差
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# 解释方差
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# 绘制输出结果~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

# ######################################################################################################################
# 机器学习模型-广义线性模型(Generalized Linear Models)（ 岭回归(Ridge Regression)）
# ######################################################################################################################

# 线性回归（岭回归）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from sklearn import linear_model

# 广义线性模型实现（岭回归）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 实例化一个 （岭回归） 类的对象
regr = linear_model.Ridge(alpha=.5)

# 在训练集上训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

# 回归模型参数查看~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
regr.coef_         # 查看变量的系数
regr.intercept_    # 查看截矩项

# ######################################################################################################################
# 机器学习模型-广义线性模型(Generalized Linear Models)（其他）
# ######################################################################################################################

from sklearn import linear_model

# 广义线性模型实现（RidgeCV）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 实例化一个 （岭回归） 类的对象
regr = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0], cv=3)

# 在训练集上训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

regr.alpha_

# 广义线性模型实现（RidgeCV）~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 实例化一个 （岭回归） 类的对象
regr = linear_model.Lasso(alpha=0.1)

# 在训练集上训练模型
regr.fit(diabetes_X_train, diabetes_y_train)

regr.predict(diabetes_X_test)



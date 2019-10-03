
# ############################
# python之加载机器学习数据集（the way of delicious easy）
# ############################
'''
上面所说的加载数据集的方式也就是使用python的sklearn库，
而且sklearn库的数据集也包含好多种：
·自带的小数据集：sklearn.datasets.load_<name>
·可在线下载的数据集：sklearn.datasets.fetch_<name>
·计算机生成的数据集：sklearn.datasets.make_<name>
·svmlight/libsvm格式的数据集：sklearn.datasets.load_svmlight_file(...)
·从data.org在线下载获取的数据集：sklearn.datastes.fetch_mldata(...)
'''

'''
除了sklearn导入之外，还可以找到所需数据集的网址，
直接用python调用网址进行加载数据集，
省去你中间下载数据集的繁琐操作
鸢尾花数据集	load_iris()
乳腺癌数据集	load_breast_cancer()
手写数字数据集	load_digits()
糖尿病数据集	load_disbetes()
波士顿房价数据集	load_boston()
体能训练数据集	load_linnerud()
'''

# ############################
# 加载鸢尾花数据集数据介绍
# ############################
from sklearn.datasets import load_iris

iris = load_iris() # 加载鸢尾花数据集
print(iris.keys()) # 输出数据集相关的操作属性，也就是“<数据集>.<操作属性>”
print('target_names', iris.target_names)
print('feature_names', iris.feature_names) # 数据属性的名称
print('DESCR', iris.DESCR) # 数据集的描述，包括这个数据集所有的相关信息

# ############################
# 实例1上手：
# ############################
from sklearn.datasets import load_iris # 导入sklearn库
import pandas as pd

iris = load_iris() # 加载鸢尾花数据集
# 将数据转为矩阵类型，也就是DataFrame,并且更改数据的列名
df_iris = pd.DataFrame(iris.data, columns=['x1', 'x2', 'x3', 'x4'])

n_samples,n_features=iris.data.shape # 数据的条数和维数
iris.data # x为数据集的属性集
iris.target # y为数据集的类别集（标签）

# 描述性统计分析
df_iris.describe().T     # 描述性统计转置

# ############################
# 通过目标数据集网址加载数据集
# ############################
'''
首先我们找到所需数据集的网址，以加载hayes-Roth数据集为例
hayes-Roth数据集的网址：https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data
'''
# 此程序必须得在联网环境下运行
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 导入hayes-roth数据集的网址
dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/hayes-roth/hayes-roth.data"

# 设置数据集的列名称，也可以不进行设置
names = ['hobby', 'age', 'educational level', 'marital status', 'class']

dataset = pd.read_csv(dataset_url, names=names)# 加载目标数据集
print(dataset.head(20))   # 输出数据集的前20行
array = dataset.values    # 拆分原始数据集
x = array[:, 0:4]         # 使x为数据集的前4列数据
y = array[:, 4]           # 使y为数据集的第5列数据
# 查看一共有几种类别以及每一种类的数量，以柱状图的形式展现出来
sns.countplot(array[:,4])

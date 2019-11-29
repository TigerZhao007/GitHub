
# ######################################################################################################################
# 连续属性离散化
# ######################################################################################################################

# 连续属性离散化方法介绍~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 离散化的需求及概念
'''
一些数据挖掘算法中，特别是某些分类算法（eg:ID3算法、Aprioroi算法等），要求数据是分类属性形式。
因此常常需要将连续属性变换成分类属性，即离散化。
离散化就是在数据的取值范围内设定若干个离散的花粉店，将取值范围划分为一些离散化的区间，
最后用不同的符号护着整数值代表落在每个区间中的数据值。
所以离散化涉及两个过程：确定分类数&将连续属性值映射到n个分类值。
'''

# 将连续数据离散化的方法，主要有三个：等宽法、等频法、聚类法
'''
等宽法是将数据的值域等分，每个部分拥有相同的宽度，然后为每个部分打上不同的符号或数值进行离散化;
等频法则是要求每个部分的记录数相同;
聚类法则是使用聚类算法比如k-means算法进行聚类获得簇，然后将合并到同一个簇做同一个标记。
三种离散化方法都需要用户指定产生的区间数
'''

# 创建测试数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np

data = np.random.rand(20)*10

# 指定区间离散化~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
label_cut = [0, 2, 4, 6, 8, 10]
data_cut = pd.cut(data, label_cut)

# 生成离散结果与原始结果对比
df_cut = pd.DataFrame({'data':data, 'data_cut':data_cut})
df_cut = df_cut.sort_values(by='data')


# 等宽离散~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 将属性的值域从最小值到最大值分成具有相同宽度的n个区间，n由数据特点决定，往往是需要有业务经验的人进行评估。
k = 5
data_cut = pd.cut(data, k, labels=range(k))

# 生成离散结果与原始结果对比
df_cut = pd.DataFrame({'data':data, 'data_cut':data_cut})
df_cut = df_cut.sort_values(by='data')

# 离散化结果可视化
def cluster_plot(d, k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(12, 4))
    for j in range(0, k):
        plt.plot(data[d == j], [j for i in d[d == j]], 'o')

    plt.ylim(-0.5, k - 0.5)
    return plt

cluster_plot(data_cut, k).show()

# 等频离散~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 将相同数量的记录放在每个区间，保证每个区间的数量基本一致。
w = [1.0*i/k for i in range(k+1)]
w = pd.DataFrame({'data': data})['data'].describe(percentiles=w)[4:4+k+2]
w[0] = w[0]*(1-1e-10)  # 由于生成的区间不包括最小值（，]
data_cut = pd.cut(list(data), w)

# 生成离散结果与原始结果对比
df_cut = pd.DataFrame({'data':data, 'data_cut':data_cut})
df_cut = df_cut.sort_values(by='data')

# 离散化结果可视化
def cluster_plot(d, k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(12, 4))
    for j in range(0, k):
        plt.plot(data[d == j], [j for i in d[d == j]], 'o')

    plt.ylim(-0.5, k - 0.5)
    return plt

cluster_plot(data_cut, k).show()

# 聚类离散~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 一维聚类离散包括两个过程：通过聚类算法（K-Means算法）将连续属性值进行聚类，
# 处理聚类之后的到的k个簇，得到每个簇对应的分类值（类似这个簇的标记）。

# 聚类离散
from sklearn.cluster import KMeans

kmodel = KMeans(n_clusters=k, n_jobs=4)  # n_jobs是并行数，一般等于CPU数
kmodel.fit(data.reshape((len(data), 1)))
c = pd.DataFrame(kmodel.cluster_centers_, columns=list('a')).sort_values(by='a')

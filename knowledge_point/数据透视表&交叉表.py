

# 创建测试数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np

date = ['2017-5-1', '2017-5-2', '2017-5-3'] * 3
rng = pd.to_datetime(date)
df1 = pd.DataFrame({'date': rng, 'key': list('abcdabcda'), 'values': np.random.rand(9)*10})

df2 = pd.DataFrame({'A': [1, 2, 2, 2, 2], 'B': [3, 3, 4, 4, 4], 'C': [1, 1, np.nan, 1, 1], 'D': [1, 1, 1, 2, 2]})

# 数据透视表 pivot_table() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False,
#                dropna=True, margins_name='All')
# data：DataFrame对象
# values：要聚合的列或列的列表
# index：数据透视表的index，从原数据的列中筛选
# columns：数据透视表的columns，从原数据的列中筛选
# aggfunc：用于聚合的函数，默认为numpy.mean，支持numpy计算方法

print(pd.pivot_table(data=df1, values='values', index='date', columns='key', aggfunc=np.sum))  # 也可以写 aggfunc='sum'
print(pd.pivot_table(data=df1, values='values', index=['date', 'key'], aggfunc=len))

# 数据交叉表 crosstab() ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 默认情况下，crosstab计算因子的频率表，比如用于str的数据透视分析
# pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False,
#             dropna=True, normalize=False)
# values：可选，根据因子聚合的值数组
# aggfunc：可选，如果未传递values数组，则计算频率表，如果传递数组，则按照指定计算
# margins：布尔值，默认值False，添加行/列边距（小计）

# 1、如果crosstab只接收两个Series，它将提供一个频率表。用A的唯一值，统计B唯一值的出现次数
print(pd.crosstab(index=df2['A'], columns=df2['B']))

# 2、以A和B界定分组，计算出每组中第三个系列C的值
print(pd.crosstab(index=df2['A'], columns=df2['B'], values=df2['C'], aggfunc=np.sum))

# 3、添加行和列边距(margins=True, margins_name='Total')
print(pd.crosstab(df2['A'], df2['B'], values=df2['C'], aggfunc=np.sum, margins=True, margins_name='Total'))

# 4、计算各列所占百分比(margins=ture, 0, 1)
print(pd.crosstab(df2['A'], df2['B'], normalize=True, margins=True, margins_name='Total'))  # 分母为所有总数
print(pd.crosstab(df2['A'], df2['B'], normalize=0, margins=True, margins_name='Total'))  # 分母为行总数
print(pd.crosstab(df2['A'], df2['B'], normalize=1, margins=True, margins_name='Total'))  # 分母为列总数

# 5、分层交叉列联表(index和columns)
# 参数index和columns可以接受列表传入，构建分层交叉表。
print(pd.crosstab(index=[df2['A'], df2['B']], columns=df2['D'], values=df2['C'], aggfunc=np.sum))
print(pd.crosstab(index=df2['A'], columns=[df2['D'], df2['B']], values=df2['C'], aggfunc=np.sum))

# 6、交叉表可视化？？？？
import seaborn as sns
df_sns = pd.crosstab(index=df2['A'], columns=df2['D'], values=df2['C'], aggfunc=np.sum)
sns.heatmap(df_sns, cmap='YlOrRd', annot=True)
sns.heatmap(df_sns, cmap='YlOrRd', annot=True, mask=df_sns < 0.1)  # 关注占比超过10%的类型

# cmap='YlOrRd'      是把颜色设置为：数值从低到高，颜色依次是黄色、橙色、红色。
# annot=True         是指在热图中保留数值。
# mask=df_sns < 0.1  是指关注占比超过10%的类型



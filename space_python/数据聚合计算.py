# -*- coding: utf-8 -*-
"""
时间：2019-11-16
作者: zuoshao（佐少）
代码说明：数据聚合计算
"""

# ######################################################################################################################
# 数据聚合计算
# https://www.cnblogs.com/splended/p/5278078.html
# ######################################################################################################################

# 创建测试数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})

people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

hier_df = pd.DataFrame(np.random.randn(4, 5),  columns=pd.MultiIndex.from_arrays(
    [['Asian', 'Asian', 'Asian', 'America', 'America'], ['China','Japan','Singapore', 'United States','Canada']],
    names=['continent', 'country']))

# groupby~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 统计分组列：['key1']，['key1', 'key2']
# 统计对象列：['data1']，['data1', 'data2']
df1 = df['data1'].groupby(df['key1']).sum().reset_index()
df1 = df.groupby(['key1'])['data1'].sum().reset_index()

df1 = df.groupby(['key1', 'key2'])['data1'].sum().reset_index()
df1 = df.groupby(['key1', 'key2'])['data1', 'data2'].sum().reset_index()

# agg~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# apply~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# mapping~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 针对不同的变量进行分组计算，将a/b/c/d//e/f变量，规整为blue/red
# 分组内容可以是字典，也可以是序列。
# axis=1， 指定按照变量分组运算。
mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red', 'f' : 'orange'}
people1 = people.groupby(mapping, axis=1).mean()

map_series = pd.Series(mapping)
people1 = people.groupby(map_series, axis=1).count()

# 通过函数进行分组~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 具体应用不清楚？？？？？？？？？
l = [len(x) for x in people.index]
people1 = people.groupby(l).count()

people1 = people.groupby(len).count()

key_list = ['one', 'one', 'one', 'two', 'two']
people1 = people.groupby([len, key_list]).min()

# 根据索引级别分组~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







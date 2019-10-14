
# ######################################################################################################################
# 基于高德地图api和Python的区县地理边界坐标提取
# ######################################################################################################################

'''
在工作中，经常想用到类似于地热图的方式进行数据展示，无法在线进行地图关联，只好自己想办法上网找边界坐标。
高德地图的api集成了这个功能，只要设置好参数就好，按照高德地图所说，按照以下三个步骤来：
第一步，申请”Web服务API”密钥（Key）；
第二步，拼接HTTP请求URL，第一步申请的Key需作为必填参数一同发送；
第三步，接收HTTP请求返回的数据（JSON或XML格式），解析数据。

高德官网的例子也说明如何访问，例如：http://restapi.amap.com/v3/config/district?keywords=北京&subdistrict=2&key=<用户的key>，对访问结果进行json解析，就可以拿到坐标啦~
key的申请方式蛮简单的，在此就不说了，以福州市为例，其下属市区有5个行政区，还有8个区县，说明下边界坐标是如何输出的~
'''

# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
# import urllib2
import numpy as np
import json
import pandas as pd
from pandas import Series, DataFrame


def getlnglat(address):
    url = 'http://restapi.amap.com/v3/config/district?'

    # 高德上申请的key
    key = '5a96233309dba9e376adfdae45a02c0a'
    uri = url + 'keywords=' + address + '&key=' + key + '&subdistrict=1' + '&extensions=all'

    # 访问链接后，api会回传给一个json格式的数据
    temp = urllib2.urlopen(uri)
    temp = json.loads(temp.read())

    # polyline是坐标，name是区域的名字
    Data = temp["districts"][0]['polyline']
    name = temp["districts"][0]['name']
    # polyline数据是一整个纯文本数据，不同的地理块按照|分，块里面的地理信息按照；分，横纵坐标按照，分，因此要对文本进行三次处理
    Data_Div1 = Data.split('|')  # 对结果进行第一次切割，按照|符号
    len_Div1 = len(Data_Div1)  # 求得第一次切割长度

    num = 0
    len_Div2 = 0  # 求得第二次切割长度，也即整个数据的总长度
    while num < len_Div1:
        len_Div2 += len(Data_Div1[num].split(';'))
        num += 1

    num = 0
    num_base = 0
    output = np.zeros((len_Div2, 5)).astype(np.float)  # 循环2次，分割；与，
    while num < len_Div1:
        temp = Data_Div1[num].split(';')
        len_temp = len(temp)
        num_temp = 0
        while num_temp < len_temp:
            output[num_temp + num_base, :2] = np.array(temp[num_temp].split(','))  # 得到横纵坐标
            output[num_temp + num_base, 2] = num_temp + 1  # 得到横纵坐标的连接顺序
            output[num_temp + num_base, 3] = num + 1  # 得到块的序号
            num_temp += 1
        num_base += len_temp
        num += 1

    output = DataFrame(output, columns=['经度', '纬度', '连接顺序', '块', '名称'])
    output['名称'] = name

    return output


def getSubName(address):  # 获取搜索区域的名称，部分区域例如鼓楼重名太多，因此返回城市代码，将城市代码作为参数给上述函数
    url = 'http://restapi.amap.com/v3/config/district?'
    key = '5a96233309dba9e376adfdae45a02c0a'
    uri = url + 'keywords=' + address + '&key=' + key + '&subdistrict=1' + '&extensions=all'
    temp = urllib2.urlopen(uri)
    temp = json.loads(temp.read())
    list0 = temp['districts'][0]['districts']
    num_Qu = 0
    output = []
    while num_Qu < len(list0):
        output.append(list0[num_Qu]['adcode'])
        num_Qu += 1

    return output

num = 0
ad = getSubName('福州')  # 得到福州下属区域的城市代码
add = getlnglat('福州')  # 得到福州整个的边界数据
while num < len(ad):
    add = pd.concat([add, getlnglat(ad[num].encode("utf-8"))])  # 得到福州下属的全部区域的边界数据
    num += 1

# add.to_csv('add.csv', encoding='gbk')  # 输出到文件






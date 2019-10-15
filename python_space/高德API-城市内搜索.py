
# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：目标地址https://www.meitulu.com/，美图录
"""

# ######################################################################################################################
# 高德地图之python爬取POI数据及其边界经纬度(根据关键字在城市范围内搜索)
# ######################################################################################################################
'''
由于之前项目需要从高德地图上爬取一个地方的不同分类数据，所以初学了一下爬虫，
也了解了一些高德地图提供的web API用来获取免费的地图数据。
项目的需求是爬取一个地方的七个分类数据， 包括大学、景点、酒店等等，其中一条数据叫作一个POI。
需要的poi点的字段包括：poi点id、名称name、位置(经纬度)location、所属省名称pname、所属省编号pcode、
所属城市名称cityname、所属城市编号citycode、所属区名称adname、所属区编号adcode、所在地址address、
所属类别type、边界经纬度。
'''

'''
步骤说明
1. 申请账号
到高德开放平台 | 高德地图API注册账号，并且申请web服务的AK密钥，每次发送请求需要带着这个key去认证。
注册账号登陆后点击右上角的控制台 ->应用管理 -> 创建应用 -> 添加新key,
注意选择web api，就得到了一个可以使用web服务的key密钥。

2. 确定api查询的地址：
查找高德地图提供的web api下的搜索模块，http://lbs.amap.com/api/webservice/guide/api/search 
使用关键字搜索服务,关键字搜索API的服务地址：http://restapi.amap.com/v3/place/text?parameters

3. API提供的参数说明
我们需要根据API提供的参数说明拼接GET请求所需要的参数URL。常用的使用参数说明：
key:用户在高德地图官网申请Web服务API类型KEY; keywords:查询关键字
types:查询POI类型; city:城市; offset,page:分页参数; output:返回数据格式类型,可选值：JSON，XML
比如，查询珠海的所有大学数据，拼接起来完整的url：
http://restapi.amap.com/v3/place/text?&keywords=%E5%A4%A7%E5%AD%A6&city=%E7%8F%A0%E6%B5%B7&output=json&offset=20&page=1&key=9f99fc570ccaf6abc209780433d9f4c1&extensions=all
使用浏览器打开上面的链接，返回的数据使用hijson格式化后截图如下：使用浏览器打开上面的链接，返回的数据使用hijson格式化后截图如下：
 其中的pois展开后就是返回的当前页的POI数据。
 
4. 根据获取到的POI数据的id获取其边界经纬度
高德地图上搜索一个景点时，如果有边界的景点会圈出其范围，
高德地图上搜索一个景点时，如果有边界的景点会圈出其范围，如下图所示：
打开F12切换到network查看，点击一下该范围，会看到发送了一个detail请求，返回了这个圈的详细信息。请求的地址如下：
https://ditu.amap.com/detail/get/detail?id=B0014014AD
该接口传入POI点的id，返回详细信息，我们在第二部拿到了POI点的ID，因此可以遍历每一个POI数据，
然后根据id获取边界数据，获取到的detail数据格式化后如下：
标红的shape数据即为边界坐标数据(一个多边形的边界其实是由多个点围成的)。
'''

# ######################################################################################################################
# 具体代码
# ######################################################################################################################
'''
getpois方法传入需要的城市名和分类关键字，最后将数据导出到d盘目录下excel文件中:
运行代码前须知:
1、需要将代码前面的amap_web_key的值替换为第一步中申请到的web api的密钥。
2、需要启动爬取程序时，需要修改getpois()方法的两个参数值(代码的后部分),
   cityname为城市名，classfield为分类名，分类可以查看官方文档。
3、由于高德地图每个key每天的请求量有限额，并且请求评率太快的话会返回错误信息，
   因此建议最好每天不要爬太多，而且不要集中在一个时间点。
'''

from urllib.parse import quote
from urllib import request
import json
import xlwt

amap_web_key = '5a96233309dba9e376adfdae45a02c0a'
poi_search_url = "http://restapi.amap.com/v3/place/text"
poi_boundary_url = "https://ditu.amap.com/detail/get/detail"

# 单页获取pois
def getpoi_page(cityname, keywords, page):
    req_url = poi_search_url + "?key=" + amap_web_key + '&extensions=all&keywords=' + quote(
        keywords) + '&city=' + quote(cityname) + '&citylimit=true' + '&offset=25' + '&page=' + str(
        page) + '&output=json'
    data = ''
    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
    return data

# 根据id获取边界数据
def getBounById(id):
    req_url = poi_boundary_url + "?id=" + id
    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
        dataList = []
        datajson = json.loads(data)  # 将字符串转换为json
        datajson = datajson['data']
        datajson = datajson['spec']
        if len(datajson) == 1:
            return dataList
        if datajson.get('mining_shape') != None:
            datajson = datajson['mining_shape']
            shape = datajson['shape']
            dataArr = shape.split(';')

            for i in dataArr:
                innerList = []
                f1 = float(i.split(',')[0])
                innerList.append(float(i.split(',')[0]))
                innerList.append(float(i.split(',')[1]))
                dataList.append(innerList)
        return dataList

# 根据城市名称和分类关键字获取poi数据
def getpois(cityname, keywords):
    i = 1
    poilist = []
    while True:  # 使用while循环不断分页获取数据
        result = getpoi_page(cityname, keywords, i)
        result = json.loads(result)  # 将字符串转换为json
        if result['count'] == '0':
            break
        poilist.extend(result['pois'])
        i = i + 1
    return poilist

# 数据写入excel
def write_to_excel(poilist, cityname, classfield):
    # 一个Workbook对象，这就相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(classfield, cell_overwrite_ok=True)
    # 第一行(列标题)
    sheet.write(0, 0, 'id')
    sheet.write(0, 1, 'name')
    sheet.write(0, 2, 'location')
    sheet.write(0, 3, 'pname')
    sheet.write(0, 4, 'pcode')
    sheet.write(0, 5, 'cityname')
    sheet.write(0, 6, 'citycode')
    sheet.write(0, 7, 'adname')
    sheet.write(0, 8, 'adcode')
    sheet.write(0, 9, 'address')
    sheet.write(0, 10, 'type')
    sheet.write(0, 11, 'boundary')
    for i in range(len(poilist)):
        # 根据poi的id获取边界数据
        bounstr = ''
        bounlist = getBounById(poilist[i]['id'])
        if (len(bounlist) > 1):
            bounstr = str(bounlist)
        # 每一行写入
        sheet.write(i + 1, 0, poilist[i]['id'])
        sheet.write(i + 1, 1, poilist[i]['name'])
        sheet.write(i + 1, 2, poilist[i]['location'])
        sheet.write(i + 1, 3, poilist[i]['pname'])
        sheet.write(i + 1, 4, poilist[i]['pcode'])
        sheet.write(i + 1, 5, poilist[i]['cityname'])
        sheet.write(i + 1, 6, poilist[i]['citycode'])
        sheet.write(i + 1, 7, poilist[i]['adname'])
        sheet.write(i + 1, 8, poilist[i]['adcode'])
        sheet.write(i + 1, 9, poilist[i]['address'])
        sheet.write(i + 1, 10, poilist[i]['type'])
        sheet.write(i + 1, 11, bounstr)
    # 最后，将以上操作保存到指定的Excel文件中
    book.save(r'd:\\' + cityname + '.xls')

# 获取城市分类数据
cityname = "珠海"
classfiled = "大学"
pois = getpois(cityname, classfiled)

# 将数据写入excel
# write_to_excel(pois, cityname, classfiled)
# print('写入成功')

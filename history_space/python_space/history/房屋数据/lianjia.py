# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:29:15 2018

@author: Think
"""

import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

# import numpy as np

item_dict1 = {
    # 标题部分
    'title': '标题', 'jianjie': '简介', 'guanzhunum': '关注人数', 'shoucangnum': '收藏人数',
    'link': '网页链接',
    # 售房信息部分
    'totleprice': '总价', 'meanprice': '单价',
    'taxprice': '税价', 'houseDate': '建成年代',
    'xiaoquname': '小区名称', 'suozaiarea': '所在区域',
    'kanfangdata': '看房时间', 'lianjiabianhao': '链家编号',

    # 基本属性部分
    'fangwuhuxing': '房屋户型', 'houseFloor': '所在楼层',
    'jianzhumianji': '建筑面积', 'huxingjiegou': '户型结构',
    'taoneimianji': '套内面积', 'buildingType': '建筑类型',
    'houseOrientation': '房屋朝向', 'jianzhujiegou': '建筑结构',
    'Decoration': '装修情况', 'tihubili': '梯户比例',
    'ladder': '配备电梯', 'chanquannianxian': '产权年限',
    'gongnuanfangshi': '供暖方式',
    # 交易属性部分
    'gaipaidata': '挂牌时间', 'jiaoyidata': '交易时间',
    'lastjiaoyidata': '上次交易', 'fangwuyongtu': '房屋用途',
    'fangwunianxian': '房屋年限', 'chanquansuoshu': '产权所属',
    'diyaxinxi': '抵押信息', 'fangbenbeijian': '房本备件',
    # 房源特色部分
    'fangyuantese': '房源特色',

    # h户型分间部分
    'huxingfenjian': '户型分间'
}


def get_url(url, headers):
    url_list = []
    resq = req.get(url, headers).content
    soup = bs(resq, 'lxml')
    lis1 = soup.find('ul', attrs={'class': 'sellListContent'})
    lis2 = lis1.find_all('div', attrs={'class': 'title'})
    for lis in lis2:
        lis3 = lis.find('a')
        url_list.append(lis3['href'])
    return url_list


def get_info(url_list, headers):
    resq = req.get(url_list, headers).content
    soup = bs(resq, 'lxml')
    item_dict = item_dict1
    # 标题部分
    lis1 = soup.find('div', attrs={'class': 'sellDetailHeader'})
    item_dict['title'] = lis1.find('h1')['title']
    item_dict['jianjie'] = lis1.find('div', attrs={'class': 'sub'})['title']
    item_dict['guanzhunum'] = lis1.find('span', attrs={'class': 'count', 'id': 'favCount'}).getText()
    item_dict['shoucangnum'] = lis1.find('span', attrs={'class': 'count', 'id': 'cartCount'}).getText()
    item_dict['link'] = url_list
    # 基本属性部分
    lis2 = soup.find('div', attrs={'class': 'base'}).find_all('li')
    item_dict['fangwuhuxing'] = lis2[0].getText().strip('房屋户型').strip()
    item_dict['houseFloor'] = lis2[1].getText().strip('所在楼层').strip()
    item_dict['jianzhumianji'] = lis2[2].getText().strip('建筑面积').strip()
    item_dict['huxingjiegou'] = lis2[3].getText().strip('户型结构').strip()
    item_dict['taoneimianji'] = lis2[4].getText().strip('套内面积').strip()
    item_dict['buildingType'] = lis2[5].getText().strip('建筑类型').strip()
    item_dict['houseOrientation'] = lis2[6].getText().strip('房屋朝向').strip()
    item_dict['jianzhujiegou'] = lis2[7].getText().strip('建筑结构').strip()
    item_dict['Decoration'] = lis2[8].getText().strip('装修情况').strip()
    item_dict['tihubili'] = lis2[9].getText().strip('梯户比例').strip()
    item_dict['ladder'] = lis2[10].getText().strip('配备电梯').strip()
    item_dict['chanquannianxian'] = lis2[11].getText().strip('产权年限').strip()
    # 交易属性部分
    lis3 = soup.find('div', attrs={'class': 'transaction'}).find_all('li')
    item_dict['gaipaidata'] = lis3[0].getText().strip('挂牌时间\n').strip()
    item_dict['jiaoyidata'] = lis3[1].getText().strip('交易权属\n').strip()
    item_dict['lastjiaoyidata'] = lis3[2].getText().strip('上次交易\n').strip()
    item_dict['fangwuyongtu'] = lis3[3].getText().strip('房屋用途\n').strip()
    item_dict['fangwunianxian'] = lis3[4].getText().strip('房屋年限\n').strip()
    item_dict['chanquansuoshu'] = lis3[5].getText().strip('产权所属\n').strip()
    item_dict['diyaxinxi'] = lis3[6].getText().strip('抵押信息\n').strip()
    item_dict['fangbenbeijian'] = lis3[7].getText().strip('房本备件\n').strip()
    # 售房信息部分
    lis4 = soup.find('div', attrs={'class': 'overview'})
    item_dict['totleprice'] = lis4.find('div', attrs={'class': 'price'}).find('span',
                                                                              attrs={'class': 'total'}).getText()
    item_dict['meanprice'] = lis4.find('div', attrs={'class': 'price'}).find('div',
                                                                             attrs={'class': 'unitPrice'}).getText()
    item_dict['taxprice'] = lis4.find('div', attrs={'class': 'price'}).find('div', attrs={'class': 'tax'}).getText()
    item_dict['houseDate'] = lis4.find('div', attrs={'class': 'area'}).find('div', attrs={'class': 'subInfo'}).getText()
    item_dict['xiaoquname'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={
        'class': 'communityName'}).getText().strip('小区名称').strip('地图')
    item_dict['suozaiarea'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={
        'class': 'areaName'}).getText().strip('所在区域').strip().replace('\xa0', '-')
    item_dict['kanfangdata'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={
        'class': 'visitTime'}).getText().strip('看房时间').strip()
    item_dict['lianjiabianhao'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={
        'class': 'houseRecord'}).getText().strip('链家编号').strip('举报')
    # 房源特色部分
    lis5 = soup.find('div', attrs={'class': 'introContent showbasemore'})
    item_dict['fangyuantese'] = lis5.getText().strip().replace('\n', '-')
    # item_dict['zhoubianpeitao'] = lis5.find_all('div',attrs={'class':'baseattribute clear'})[0].getText().strip('周边配套\n').strip()
    # item_dict['xiaoqujieshao'] = lis5.find_all('div',attrs={'class':'baseattribute clear'})[2].getText().strip('小区介绍\n').strip()
    # item_dict['jiaotongchuxing'] = lis5.find_all('div',attrs={'class':'baseattribute clear'})[3].getText().strip('交通出行\n').strip()
    # item_dict['hexinmaidian'] = lis5.find_all('div',attrs={'class':'baseattribute clear'})[4].getText().strip('核心卖点\n').strip()
    # 房源特色部分
    lis6 = soup.find('div', attrs={'class': 'layout-wrapper'}).find('div', attrs={'class': 'info'})
    item_dict['huxingfenjian'] = lis6.getText().strip().replace('\n', '-')
    return item_dict
def main():
    item = []
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    for i in range(1,2):
        url = 'https://nj.lianjia.com/ershoufang/gulou/pg%s/'%(i)
        print('--------------------------------------------------')
        print('正在爬取第%s页信息'%(i))
        url_list = get_url(url,headers)
        for url in url_list:
            print('正在爬取%s信息'%(url))
            item.append(get_info(url,headers))
    item1 = pd.DataFrame(item)
    item1.to_csv('C:/Users/Think/Desktop/gulou.csv')
    print('成功保存gulou地区数据')

if __name__ == '__main__':
	main()

'''
item = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
for i in range(1,2):
     url = 'https://nj.lianjia.com/ershoufang/gulou/pg%s/'%(i)
     print('--------------------------------------------------')
     print('正在爬取第%s页信息'%(i))
     url_list = get_url(url,headers)
     for url in url_list:
         print('正在爬取%s信息'%(url))
         item.append(get_info(url,headers))
item1 = pd.DataFrame(item)
item1.to_csv('C:/Users/Think/Desktop/gulou.csv')
print('成功保存gulou地区数据')  
'''






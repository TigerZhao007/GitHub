# -*- coding: utf-8 -*-
"""
Created on Wed May  2 00:38:49 2018

@author: Think
"""


from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver  



item = {
    'name':'模特姓名',
    'link':'链接后缀',
    'img':'图片概览',
    'data':'浏览评论数据'
}
item = pd.DataFrame.from_dict(item,orient='index').T

url_list = ['http://www.lesmao.me/forum-UGirls-%s.html'%(str(num))
        for num in range(1,14)]
browser = webdriver.PhantomJS(executable_path="D:/Python/selenium/webdriver/phantomjs/bin/phantomjs.exe")  

item_list = pd.DataFrame()
for url in url_list:
    print('正在加载%s信息'%(url))
    browser.get(url)
    data = browser.page_source
    soup = bs(data,'lxml')
    lis1 = soup.find('div',attrs={'class':'cl listpic'}).find_all('div',attrs={'class','group'})
    for lis in lis1:
        item['link'] = lis.find('a')['href']
        item['name'] = lis.find('img')['alt']
        item['img'] = lis.find('img')['src']
        item['data'] = lis.find('div',attrs={'class':'data'}).getText().strip()
        item_list = item_list.append(item)
item_list.to_csv("C:/Users/Think/Desktop/test.csv",index=False,sep=',')
print('成功保存gulou地区数据')











# -*- coding: utf-8 -*-
"""
Created on Thu May  3 00:23:45 2018

@author: Think
"""

from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver  
import re
import urllib


#url = 'http://www.lesmao.me/forum-UGirls-1.html'
url_list = ['http://www.lesmao.me/forum-UGirls-%s.html'%(str(num))
        for num in range(1,15)]
#url_list


item = {
    'name':'模特姓名',
    'link':'链接后缀',
    'img':'图片概览',
    'data':'浏览评论数据'
}
item = pd.DataFrame.from_dict(item,orient='index').T

# @brief 保存图片 # url : 图片url # addr  : 保存的地址
def save_picture(url,addr,name):
    urllib.request.urlretrieve(url,'{}{}.jpg'.format(addr,name))    
    return

browser = webdriver.PhantomJS(executable_path="D:/Python/selenium/webdriver/phantomjs/bin/phantomjs.exe")  

item_list = pd.DataFrame()
for url in url_list:
    print('--------------------------------------------------------')
    print('正在加载%s信息'%(url))
    browser.get(url)
    data = browser.page_source
    soup =  BeautifulSoup(data,'lxml')
    lis1 = soup.find('div',attrs={'class':'cl listpic'}).find_all('div',attrs={'class','group'})
    for lis in lis1:        
        reg = r'thread-(.+?)-1'
        imgre = re.compile(reg)
        imglist = lis.find('a')['href']
        item['link'] = imgre.findall(imglist)
        item['name'] = lis.find('img')['alt']
        item['img'] = lis.find('img')['src']
        item['data'] = lis.find('div',attrs={'class':'data'}).getText().strip()
        item_list = item_list.append(item)

driver = webdriver.PhantomJS(executable_path="D:/Python/selenium/webdriver/phantomjs/bin/phantomjs.exe")  
path = 'C:\\Users\\Think\\Desktop\\pythondownload\\'

for link in item_list['link']:
    j = 1
    for num in range(1,6):
        url1 = 'http://www.lesmao.me/thread-' + link + '-%s-1.html'%str(num)
        print('正在加载图片%s'%(url1))
        driver.get(url1)
        data = driver.page_source
        soup = BeautifulSoup(data,'lxml')
        lis1 = soup.find('div',attrs={'id':'thread-pic'}).find_all('li')
        for lis in lis1:
            picture = lis.find('img')['src']
            save_picture(picture,path,str(link)+'_'+str(j))
            j += 1
        









# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from lxml import etree
import pandas as pd
from selenium import webdriver
import re
import urllib
import time
import os

# 获取所有图片链接url_list
#browser = webdriver.PhantomJS(executable_path="D:/Python/selenium/webdriver/phantomjs/bin/phantomjs.exe")
#browser.get('http://www.mzitu.com/')
#html = browser.page_source
#selector = etree.HTML(html)
#pagenum = selector.xpath('/html/body/div[2]/div[1]/div[2]/nav/div/a[4]/@href')[0].strip('http://www.mzitu.com/page/').strip('/')
url_list = ['http://www.mzitu.com/']+['http://www.mzitu.com/page/%s/'%(str(num)) for num in range(2,int(180)+1)]

# 设置图片存储路径
path_info = 'E:\Downloads\picture\data_information'
path = 'E:/Downloads/picture/妹子图meizitu/'
# 创建文件夹
try:
    os.mkdir(path)
except:
    pass
# @brief 保存图片  # url : 图片url # addr  : 保存的地址
def save_picture(url,addr,name,num):
    headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/65.0.3325.181 Safari/537.36',
                 'Referer': "http://www.mzitu.com"}
    picture = requests.get(url,headers=headers,stream=True)
    path = addr + name + str(num)+ '.jpg'
    with open(path, 'wb')as f:
        f.write(picture.content)
        #print("正在保存{}第{}张".format(self.girl_name, img_name))
        f.close()

# 详情信息info
item = {
    'name':'标题',
    'link':'链接',
    'date':'发布日期',
    'data':'浏览数量'
}
item = pd.DataFrame.from_dict(item,orient='index').T

# 获取详情信息info
browser = webdriver.PhantomJS(executable_path="D:/Python/selenium/webdriver/phantomjs/bin/phantomjs.exe")
item_list = pd.DataFrame()
for url in url_list:
    print('--------------------------------------------------------')
    print('正在加载%s信息'%(url))
    time.sleep(3)
    browser.get(url)
    data = browser.page_source
    soup =  BeautifulSoup(data,'lxml')
    try:
        lis1 = soup.find('div',attrs={'class':'main'}).find('ul',attrs={'id':'pins'}).find_all('li')
    except:
        lis1 = []
        print('加载失败')
    for lis in lis1:
        try:
            item['link'] = lis.find('a')['href'].strip(' ')
            item['name'] = lis.find('img')['alt'].strip(' ').replace("!",'').replace("！",'').replace(",",'').replace("，",'').replace(" ",'').replace(" ",'').replace("？",'').replace("\"",'')
            item['date'] = lis.find_all('span')[1].getText().strip('发布').strip(' ')
            item['data'] = lis.find_all('span')[2].getText().strip('浏览(').strip(')').strip('次').strip(' ')
            item_list = item_list.append(item)
        except:
            print('加载失败')

# 获取详情页图片
driver = webdriver.PhantomJS(executable_path="D:/Python/selenium/webdriver/phantomjs/bin/phantomjs.exe")
item_flase = pd.DataFrame()

print('----------------------第一阶段------------------------')

for i in range(len(item_list)-11,len(item_list)):
    url1 = item_list['link'].iloc[i]
    name = item_list['name'].iloc[i]
    print('---------------------------------------------%s---%s---%s'%(i,len(item_list),i/len(item_list)))
    print('正在加载图片%s'%(url1))
    j = 1
    try:
        driver.get(url1)
        html = driver.page_source
        selector = etree.HTML(html)
        maxnum = selector.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')[0]
        url_list = ['%s/%s'%(url1,str(num)) for num in range(1,int(maxnum)+1)]
        for url2 in url_list:
            driver.get(url2)
            time.sleep(1)
            html = driver.page_source
            selector = etree.HTML(html)
            pic_urls = selector.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')
            save_picture(pic_urls[0],path,name,j )
            j += 1
    except:
        item_flase = item_flase.append(item_list.iloc[i,:])
        print('加载失败')




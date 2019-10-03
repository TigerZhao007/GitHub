# -*- coding: utf-8 -*-
"""
Created on Wed May  2 00:38:49 2018

@author: Think
"""

import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import csv 
from selenium import webdriver  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import sys


item = {
    'area':'地区',
    'year':'年份',
    'type':'学生类型',
    'time':'批次',
    'line':'分数线'
}
item = pd.DataFrame.from_dict(item,orient='index').T

url_list = ['http://gkcx.eol.cn/soudaxue/queryProvince.html?page='+ str(num)
        for num in range(1,166)]
browser = webdriver.PhantomJS(executable_path="D:/Python/selenium/webdriver/phantomjs/bin/phantomjs.exe")  

item_list = pd.DataFrame()
for url in url_list:
    print('正在加载%s信息'%(url))
    browser.get(url)
    data = browser.page_source
    soup = bs(data,'lxml')
    lis1 = soup.find('div',attrs={'class':'lin-seachcol-table lin-placegrade-table'}).find('tbody',attrs={'class':'lin-seachtable'}).find_all('tr')
    for lis in lis1:
        lis2 = lis.find_all('td')
        item1 = item
        item1['area'] = lis2[0].getText()
        item1['year'] = lis2[1].getText()
        item1['type'] = lis2[2].getText()
        item1['time'] = lis2[3].getText()
        item1['line'] = lis2[4].getText()
        item_list = item_list.append(item)
item_list.to_csv("C:/Users/Administrator.USER-20161208UW/Desktop/test.csv",index=False,sep=',')
print('成功保存gulou地区数据')











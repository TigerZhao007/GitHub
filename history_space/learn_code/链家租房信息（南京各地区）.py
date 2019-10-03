# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:13:40 2017

@author: Administrator
"""

import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

## 链家网连接
url = 'https://nj.lianjia.com/zufang/gulou/pg'+ str(1) + 'rco10/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
      		}

## 爬取列表连接
def get_link(url,headers):
   resp = requests.get(url,headers).content
   soup = BeautifulSoup(resp, 'lxml')
   dat1 = soup.find_all('div',attrs={'class':'pic-panel'})
   dat2 = re.findall(r'a href="(.+?)" target="_blank"',str(dat1))
   return dat2

## 爬取列表单个连接内容
def get_house_basic(url,headers):
   resp = requests.get(url,headers).content
   soup = BeautifulSoup(resp, 'lxml')
   dat1 = soup.find_all('div',attrs={'class':'zf-room'})
   lis_num = []
   for i in range(0,len(dat1)):
       a = dat1[i].getText().split()
       lis_num.append(a)
       dat_xiaoqu = re.findall(r'小区：(.+?)\',',str(lis_num[0]))[0]
       dat_ditie  = re.findall(r'地铁：(.+?)\',',str(lis_num[0]))[0]
       dat_weizhi = re.findall(r'位置：(.+?)\',',str(lis_num[0]))[0]
       dat_louceng= re.findall(r'楼层：(.+?)\',',str(lis_num[0]))[0]
       dat_fangxiang = re.findall(r'房屋朝向：(.+?)\',',str(lis_num[0]))[0]
       dat_ceng  = re.findall(r'(共(.+?)层)',str(lis_num[0]))[0]
       dat_link = url
       dat2 = [dat_xiaoqu,dat_ditie,dat_weizhi,dat_louceng,dat_ceng,dat_fangxiang,dat_link]
   return dat2

## 主函数
def write_dat(area,n):
   print('正在读取%s页的文本' % (area))
   f1 = open(r'C:\\Users\\Administrator\\Desktop\\%s.csv'%(area),'a')
   headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
      }
   for i in range(n):
       url = 'https://nj.lianjia.com/zufang/%s/pg'%(area) + str(i) + 'rco10/'
       print('正在读取%s页的文本' % (i+1))
       df0 = get_link(url,headers)
       for df in df0:
           print('正在读取%s的文本' % (df))
           df1 = get_house_basic(df,headers)
           f1.writelines(str(df1)+'\n')
           print('---------------------------------------成功保存文本')
   f1.close()

def main(): 
    area_total = ['gulou','jianye','qinhuai','xuanwu','yuhuatai','qixia','jiangning','pukou']
    n_total    = ['48','24','44','30','18','27','65','40']
    for k in range(0,len(n_total)): 
        area = area_total[k]
        n    = int(n_total[k])
        write_dat(area,n)

## 执行主函数
if __name__ == '__main__':
	main()












# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 00:24:36 2018

@author: Think
"""

import requests
import re
import urllib
import requests
import pandas as pd
from bs4 import BeautifulSoup


# @brief  打开网页 # url : 网页地址# @return 返回网页数据
def getHtmlText(url,headers):
    try:
        r = requests.get(url, headers,timeout=30)  # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()               # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"

 # 找图片
def getImg(html):
#    reg = r'src="(.+?\.jpg)" pic_ext'
    reg = r'src="(.+?\.jpg)"'
#    reg = r'src="(.+?\.jpg)" style'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)                       #表示在整个网页中过滤出所有图片的地址，放在imglist中
    return imglist

# @brief 保存图片 # url : 图片url # addr  : 保存的地址
def save_picture(url,addr,name):
    urllib.request.urlretrieve(url,'{}{}.jpg'.format(addr,name))    
    return

def get_link(url,headers):
   resp = requests.get(url,headers).content
   soup = BeautifulSoup(resp, 'lxml')
   dat1 = soup.find_all('li',attrs={'class':'zxsyt'})
   url_list = re.findall(r'a href="/html/PIC06/(.+?).html" target="_blank"',str(dat1))
   name_list = re.findall(r'target="_blank">(.+?)</a>',str(dat1))
   bisic = [url_list,name_list]
   return bisic

def main():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    path = 'C:\\Users\\Think\\Desktop\\pythondownload\\'
    for i in range(60):
        try:
#            url1 = 'http://39td.com/PIC06/list_%s.html'%i
            url1 = 'http://39td.com/PIC06/list_%s.html'%i
            print("正在爬取第%s页图片"%i)
            url_list = get_link(url1,headers)
            for url in url_list[0]:
                url2 = 'http://39td.com/html/PIC06/%s.html'%url
                html = getImg(getHtmlText(url2,headers))#获取该网址网页详细信息，得到的html就是网页的源代码
                j = 1
                for html_url in html:
                    save_picture(html_url,path,str(url)+'_'+str(j))
                    #print('成功保存第%s张图片'%j)
                    j += 1
        except:
            print('没有保存第%s页图片'%i)

if __name__ == '__main__':
	main()
			
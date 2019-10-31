# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 23:24:32 2018

@author: Think
"""

import requests
import re
import urllib

# @brief  打开网页 # url : 网页地址# @return 返回网页数据
def getHtmlText(url,headers):
    try:
        r = requests.get(url, headers, timeout=30)  # 如果状态码不是200 则应发HTTOError异常
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

def main():
#    url = "http://tieba.baidu.com/p/2460150866"
#    url = "https://tieba.baidu.com/p/1457328431"
    url = 'http://www.lesmao.me/thread-18050-1-1.html'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    path = 'C:\\Users\\Think\\Desktop\\pythondownload\\' 
    html = getImg(getHtmlText(url,headers))#获取该网址网页详细信息，得到的html就是网页的源代码
    j = 0
    for html_url in html:
        save_picture(html_url,path,j)
        print('成功保存第%s张图片'%j)
        j += 1

    
if __name__ == '__main__':
	main()
			


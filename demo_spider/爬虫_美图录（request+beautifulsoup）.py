# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：目标地址https://www.meitulu.com/，美图录
"""

# 请求网页数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getHtmlText(url):
    ''' # url:网页地址; # return:返回网页数据 '''

    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import requests
    import random

    # 设置表头~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                            "Chrome/63.0.3239.132 Safari/537." + str(random.randint(1, 99))
    # headers['Referer'] = url

    # 读取HTML文本~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try:
        r = requests.get(url, headers, timeout=30)  # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()               # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"

# 指定某一页，统计该页信息~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getImgList(html):

    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import pandas as pd
    from bs4 import BeautifulSoup as bs

    # 导入图片列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    soup = bs(html, 'lxml')
    soup = soup.find('div', attrs={'class': 'main'}).find('ul', attrs={'class': 'img'})
    soup = soup.find_all('li')     # 表示在整个网页中过滤出所有图片的地址，放在imglist中
    namelist = ['model_name', 'pic_name', 'pic_num', 'pic_agent', 'pic_label', 'pic_url']
    imglist = pd.DataFrame(columns=namelist)

    # 统计列表信息~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for img in soup:
        imgdict = {}
        imgdict['pic_url'] = img.find('a')['href']
        imgdict['pic_name'] = img.find('img')['alt']
        imgdict['pic_num'] = img.find_all('p')[0].text.replace('数量：','')
        imgdict['pic_agent'] = img.find_all('p')[1].text.replace('机构：','')
        imgdict['model_name'] = img.find_all('p')[2].text.replace('模特：','')
        imgdict['pic_label'] = img.find_all('p')[3].text.replace('标签：','')
        imgdict = pd.DataFrame([imgdict])[namelist]
        imglist = imglist.append(imgdict)

    return imglist

# 爬虫代码汇总~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(url, tablename):
    import sqlalchemy
    engine = sqlalchemy.create_engine("postgresql://postgres:123456@106.12.30.122:5432/test",
                                      pool_size=20, max_overflow=5)
    html = getHtmlText(url)
    imglist = getImgList(html)

    with engine.connect() as conn:
        imglist.to_sql(tablename, conn, if_exists='append', index=False)

# 主函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':

    import time
    t1 = time.time()

    url_list = ['https://www.meitulu.com/guochan/%s.html' %(x) for x in range(2, 191)]
    for url in url_list:
        main(url, tablename='meitulu_single')

    t2 = time.time()
    print("总耗时：%.2f 秒"%(t2-t1))


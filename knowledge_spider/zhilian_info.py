# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：目标地址https://www.meitulu.com/，美图录
"""

# 请求网页数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getHtmlText(url):
    ''' # url:网页地址; # return:返回网页数据 '''

    # url = 'https://sou.zhaopin.com/?p=6&jl=635&kw=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&kt=3&sf=0&st=0'
    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import requests
    import random

    # 设置表头~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                            "Chrome/63.0.3239.132 Safari/537." + str(random.randint(1, 99))

    # 读取HTML文本~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try:
        # r = requests.get(url, headers, timeout=10)  # 如果状态码不是200 则应发HTTOError异常
        r = requests.get(url, timeout=10)
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
        temp = img.find_all('p')[0].find('span').text
        imgdict['pic_num'] = img.find_all('p')[0].text.replace('数量：', '').replace(temp, '')
        # imgdict['pic_num'] = img.find_all('p')[0].text.replace('数量：', '')
        imgdict['pic_agent'] = img.find_all('p')[1].text.replace('机构：','')
        imgdict['model_name'] = img.find_all('p')[2].text.replace('模特：','')
        imgdict['pic_label'] = img.find_all('p')[3].text.replace('标签：','')
        imgdict = pd.DataFrame([imgdict])[namelist]
        imglist = imglist.append(imgdict)

    return imglist

# 爬虫代码汇总~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(url):
    import sqlalchemy
    import pandas as pd

    engine = sqlalchemy.create_engine("postgresql://postgres:123456@47.100.173.196:5432/project_spider",
                                      pool_size=20, max_overflow=5)

    # 获取指定页图片列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    html = getHtmlText(url)
    picture_info = getImgList(html)
    picture_info['is_download'] = 'flase'

    # 获取指定页图片列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try:
        sql = ''' SELECT pic_url FROM public.meitulu_picture_info_v02 '''
        with engine.connect() as conn:
            imglist_in = tuple(list(pd.read_sql_query(sql, conn)['pic_url']))

        picture_info = picture_info[~picture_info['pic_url'].isin(imglist_in)]

    except:
        pass

    with engine.connect() as conn:
        picture_info.to_sql('meitulu_picture_info_v02', conn, if_exists='append', index=False)

# 主函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':

    import time
    t1 = time.time()
    list_false = []

    # name_list = ['rihan', 'gangtai', 'guochan']
    url_list = ['http://www.meitulu.cn/rihan/'] + \
               ['http://www.meitulu.cn/rihan/index_%s.html' %(x) for x in range(2, 50)] + \
               ['http://www.meitulu.cn/gangtai/'] + \
               ['http://www.meitulu.cn/gangtai/index_%s.html' % (x) for x in range(2, 50)] + \
               ['http://www.meitulu.cn/guochan/'] + \
               ['http://www.meitulu.cn/guochan/index_%s.html' % (x) for x in range(2, 50)]

    for url in url_list:
        try:
            print('正在处理连接：%s......' %(url))
            main(url)
            time.sleep(1)  # 推迟一秒
        except:
            list_false = list_false + [url]

    t2 = time.time()
    print("总耗时：%.2f 秒"%(t2-t1))


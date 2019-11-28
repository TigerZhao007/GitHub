
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
    # headers['Referer'] = '''https://www.meitulu.com/t/nvshen/'''
    # headers['Accept'] = '''text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'''
    # headers['Accept-Encoding'] = '''gzip, deflate, br'''
    # headers['Accept-Language'] = '''zh-CN,zh;q=0.9'''
    # headers['Host'] = '''www.meitulu.com'''
    # headers['Cache-Control'] = '''max-age=0'''
    # headers['Connection'] = '''keep-alive'''
    # headers['If-None-Match'] = '''"5dd5e305-de19"'''
    # headers['Sec-Fetch-Mode'] = '''navigate'''
    # headers['Sec-Fetch-Site'] = '''none'''
    # headers['Sec-Fetch-User'] = '''?1'''
    # headers['Upgrade-Insecure-Requests'] = '''1'''
    # headers['Cookie'] = '''UM_distinctid=16dc50e174c278-024a8d7adaa2b7-7373e61-144000-16dc50e174d1a8; CNZZDATA1255487232=939500139-1570975242-%7C1570975242; CNZZDATA1255357127=771937645-1570965867-https%253A%252F%252Fwww.baidu.com%252F%7C1574603813'''

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
        imgdict['pic_num'] = img.find_all('p')[0].text.replace('数量：','')
        imgdict['pic_agent'] = img.find_all('p')[1].text.replace('机构：','')
        imgdict['model_name'] = img.find_all('p')[2].text.replace('模特：','')
        imgdict['pic_label'] = img.find_all('p')[3].text.replace('标签：','')
        imgdict = pd.DataFrame([imgdict])[namelist]
        imglist = imglist.append(imgdict)

    return imglist

# 图片详情页最大页码~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getPicNum(html_pic):
    ''' # url:网页地址; # return:返回网页数据 '''

    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import pandas as pd
    from bs4 import BeautifulSoup as bs

    # 导入图片列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    soup = bs(html_pic, 'lxml')
    max_page = soup.find('div', attrs={'id': 'pages'}).find_all('a')[-2].text

    return max_page

# 图片详情页列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getPicList(html_pic):
    ''' # url:网页地址; # return:返回网页数据 '''

    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import pandas as pd
    from bs4 import BeautifulSoup as bs

    # 导入图片列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    soup = bs(html_pic, 'lxml')
    soup = soup.find('div', attrs={'class': 'content'}).find_all('img')
    pic_list = [x['src'] for x in soup]
    pic_name = [x['alt'] for x in soup]
    pic_dict = {'pic_list':pic_list, 'pic_name':pic_name}

    return pic_dict

# 图片详情页列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def downloadPic(path, pic_url, pic_name):

    '''
    :param path: # path = r'D:\Desktop'
    :param pic_url: # pic_url = 'https://mtl.gzhuibei.com/images/img/17827/4.jpg'
    :param pic_name: # pic_name = 'a'
    :return: 返回网页数据
    '''

    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import requests

    # 导入图片列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    r = requests.get(pic_url).content
    path = path + '\\' + pic_name.replace('/', '').replace('\\', '') + '.jpg'

    try:
        with open(path, 'wb') as f:
            f.write(r)
            # print('保存成功 %s.jpg' % pic_name)
    except:
        print('保存失败')

# 设置桌面路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_desktop():
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
    return desktop_path

# 新加存储路径~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mkdir(path):
    import os    # 引入模块
    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    isExists = os.path.exists(path)  # 判断路径是否存在, 存在-True, 不存在-False
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录, 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

# 爬虫代码汇总~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main(img_url):
    import sqlalchemy
    import pandas as pd

    engine = sqlalchemy.create_engine("postgresql://postgres:123456@47.100.173.196:5432/project_spider",
                                      pool_size=20, max_overflow=5)
    path = get_desktop() + '\\pic_file'
    mkdir(path=path)

    list_false = []

    try:
        print('正在处理页码：%s' % (img_url))
        img_lis = getHtmlText(img_url)
        img_num = getPicNum(img_lis)
        img_lis = [img_url] + [img_url.replace('.html', '') + '_' + str(x) + '.html' for x in range(2, int(img_num)+1)]

        for img_li in img_lis:
            try:
                img_info = getHtmlText(img_li)
                img_info = getPicList(img_info)

                for pic_list, pic_name in zip(img_info['pic_list'], img_info['pic_name']):
                    # print(pic_name)
                    try:
                        downloadPic(path=path, pic_url=pic_list, pic_name=pic_name)
                    except:
                        pass
            except:
                pass

        sql = '''update public.meitulu_picture_info_v01 set is_download='true' where pic_url='%s' ''' % (img_url)
        with engine.connect() as conn:
            conn.execute(sql)

    except:
        list_false = list_false + [img_lis]

    return list_false

# 主函数~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':

    import time
    import sqlalchemy
    import pandas as pd

    t1 = time.time()
    list_false = []

    engine = sqlalchemy.create_engine("postgresql://postgres:123456@47.100.173.196:5432/project_spider",
                                      pool_size=20, max_overflow=5)

    sql = '''select distinct pic_url FROM public.meitulu_picture_info_undownload_v01'''
    with engine.connect() as conn:
        url_list = list(pd.read_sql_query(sql, conn)['pic_url'])

    i = 1
    for img_url in url_list:
        try:
            main(img_url=img_url)
            if i % 100 == 0:
                time.sleep(120)
            else:
                time.sleep(1)
        except:
            list_false = list_false + [img_url]

    t2 = time.time()
    print("总耗时：%.2f 秒"%(t2-t1))


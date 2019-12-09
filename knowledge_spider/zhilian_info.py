# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：目标地址https://www.meitulu.com/，美图录
"""

# 请求网页数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getHtmlText(url):
    ''' # url:网页地址; # return:返回网页数据 '''

    # url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试&kt=3'
    # url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3'
    # url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&start=0&areaId=&businessarea=%7B%7D&industry=100010000&salary=0,0&jobType=&sortType='
    # url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=801&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&start=&areaId=&businessarea=&industry=&salary=&jobType=&sortType='
    # '&start=0&areaId=&businessarea=%7B%7D&industry=100010000&salary=0,0&jobType=&sortType='
    # url = 'https://fe-api.zhaopin.com/c/i/sou/page-title?start=0&pageSize=90&cityId=801&areaId=&businessarea=%7B%7D&industry=100010000&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=-1&sortType=&kw=Java%E5%BC%80%E5%8F%91&kt=3&bj=&sj=&lastUrlQuery=%7B%22jl%22:%22801%22,%22in%22:%22100010000%22,%22sf%22:0,%22st%22:0,%22kw%22:%22Java%E5%BC%80%E5%8F%91%22,%22kt%22:%223%22%7D&companyNo=&companyName=&_v=0.11437274&x-zp-page-request-id=0c3d788750314427b8f18fb983320a60-1575907790349-652696&x-zp-client-id=6b10dda1-77fc-43c1-afa8-b2bff9969ccb&MmEwMD=415kLLzl0LAscQHnpkjFQOZ7cCPOH4LiUYFR6qgEynlVIN9mZiUw0DIwVREpxsCr4BJnjds7FRmuXset_10NVHB6R4LhFcJZzjl9sY7ymG6f1vA_xkeUm5px8zB2WGPzd.XT.0yaA2hLF4sVUhRv3DExDjYNzKGs1Tqh9oICsNOtQxmiBXoQXncx3kliILX5ju5iORGq9B3p5AMZ2PDN8sqhxLhzRes6ecUOF7nbv2nbmOZi8lUG3vQGHETa.vXQCBl9EXthr815CjiaN7ub6ZOXE5OVTsVW.PdAAIj81OhNgB7e38Mx.x2EVEd9yt0EAgKOJAiV10xnzYWFRCUz2MMS0F9tgbfEi8vZ_AXnkFUoPGfrdAcjvkbHjcAsGywT254dqLo8A.qviwlRSkaJo5Fw5'

    params = {
        "pageSize": "90",
        "cityId": "801",
        "industry": "100010000",
        "salary": "0,0",
        "workExperience": "-1",
        "education": "-1",
        "companyType": "-1",
        "employmentType": "-1",
        "jobWelfareTag": "-1",
        "kw": "Java开发",
        "kt": "3",
        "_v": "0.75694563"
    }

    url = 'https://fe-api.zhaopin.com/c/i/sou'

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
        r = requests.get(url, params=params, headers=headers, timeout=10)  # 如果状态码不是200 则应发HTTOError异常
        # r = requests.get(url, timeout=10)
        # r.raise_for_status()               # 设置正确的编码方式
        # r.encoding = r.apparent_encoding
        # return r.text
        r.json()
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


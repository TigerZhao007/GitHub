# -*- coding: utf-8 -*-
"""
时间：2019-10-13
作者: zuoshao（佐少）
代码说明：目标地址https://www.meitulu.com/，美图录
"""

# 请求网页数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getHtmlText(start, pageSize):
    ''' # url:网页地址; # return:返回网页数据 '''

    params = {"cityId": "801", "industry": "100010000",  "salary": "0,0",  "workExperience": "-1", "education": "-1",
              "companyType": "-1",  "employmentType": "-1",  "jobWelfareTag": "-1", "kw": "Java开发",
              "kt": "3",  "_v": "0.75694563"}
    params['start'] = start
    params['pageSize'] = pageSize

    url = 'https://fe-api.zhaopin.com/c/i/sou'

  # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import requests
    import random

    # 设置表头~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                            "Chrome/63.0.3239.132 Safari/537." + str(random.randint(1, 99))
    headers['Origin'] = "https://sou.zhaopin.com"

    # 读取HTML文本~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)  # 如果状态码不是200 则应发HTTOError异常
        result = r.json()
        return result
    except:
        return "Something Wrong!"

html = getHtmlText(start=0, pageSize=90)

# 指定某一页，统计该页信息~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getImgList(html):

    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import pandas as pd
    import json

    # 导入图片列表~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    result = html.get('data').get('results')

    # 统计列表信息~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    return result

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


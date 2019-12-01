
url = 'https://www.itjuzi.com/api/closure?com_prov=&sort=&page=1&keyword=&cat_id='
url = 'https://www.itjuzi.com/api/closure?com_prov=&fund_status=&sort=&page=1'
# 请求网页数据~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getHtmlText(url):
    ''' # url:网页地址; # return:返回网页数据 '''

    # url = 'http://www.meitulu.cn/rihan/index_2.html'
    # 导入所需模块~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    import requests
    import random

    # 设置表头~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    headers['Referer'] = 'https://www.itjuzi.com/deathCompany'
    headers['Host'] = 'www.itjuzi.com'
    headers['Cookie'] = '_ga=GA1.2.2145505341.1575179713; _gid=GA1.2.1932019616.1575179713; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1575179713; _gat_gtag_UA_59006131_1=1; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1575182540'
    # headers['Referer'] = ''
    # headers['Referer'] = ''
    # headers['Referer'] = ''
    # headers['Referer'] = ''

    # 读取HTML文本~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    try:
        r = requests.get(url, headers)  # 如果状态码不是200 则应发HTTOError异常
        # r = requests.get(url, timeout=10)
        r.raise_for_status()               # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"

html = getHtmlText(url)
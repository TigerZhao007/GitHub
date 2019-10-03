import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver

# ----------------------------URL-----------------------------
start = '2015-10-13'
end = '2018-10-29'

datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
url_list = []
while datestart < dateend:
    datestart += datetime.timedelta(days=1)
    url_list.append(datestart.strftime('%Y%m%d'))

url_list = ['https://bcy.net/coser/toppost100?type=lastday&date=%s'%(date) for date in url_list]

# ----------------------------headers-----------------------------
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# ----------------------------path-----------------------------
# 设置图片存储路径
path = 'E:/Downloads/picture/半次元bcynet/'
# 创建文件夹
try:
    os.mkdir(path)
except:
    pass
# @brief 保存图片  # url : 图片url # addr  : 保存的地址
def save_picture(url,addr,name,num):
    headers = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/65.0.3325.181 Safari/537.36',
                 'Referer': "http://www.mmjpg.com"}
    picture = requests.get(url,headers=headers)
    path = addr + name + str('-') + str(num) + '.jpg'
    with open(path, 'wb')as f:
        f.write(picture.content)
        #print("正在保存{}第{}张".format(self.girl_name, img_name))
        f.close()


# ---------------------------for----------------------------------
# 循环每天今日热门，得到每日TOP50的URL
browser = webdriver.PhantomJS(executable_path="D:/python/phantomjs/bin/phantomjs.exe")

for url in url_list:
    print('-----------------------------------------------------')
    print('正在加载'+ url)
    try:
        resq = requests.get(url, headers).content
        soup = BeautifulSoup(resq, 'lxml')
        lis = soup.find('ul', attrs={'class': 'l-clearfix gridList smallCards js-workTopList'}).find_all('li')

        # 循环每日TOP50的URL， 得到具体链接URL
        for li in lis:
            try:
                url_detail = li.find('a')['href']
                name = url_detail.replace('/item/detail/', '')
                url_detail = ['https://bcy.net%s' % (url_detail)]

                # browser = webdriver.PhantomJS(executable_path="D:/python/phantomjs/bin/phantomjs.exe")
                browser.get(url_detail[0])
                data = browser.page_source
                soup_detail = BeautifulSoup(data, 'lxml')

                lis_detail = soup_detail.find('div', attrs={'class': 'album'})
                lis_detail = lis_detail.find_all('img')
                lis_detail = lis_detail[1:]
                # print(lis_detail)

                try:
                    # 循环每个详细网页，得到每张图片链接URL
                    j = 1
                    for pic in lis_detail:
                        pic = pic['src']
                        save_picture(pic, path, name, j)
                        print(pic)
                        j += 1
                except:
                    pass
            except:
                pass
    except:
        pass






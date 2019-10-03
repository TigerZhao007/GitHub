import scrapy
from lianjia.items import LianjiaItem
from bs4 import BeautifulSoup
import time
import requests

class firstSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["nj.lianjia.com/"]
    start_urls = [
         'https://nj.lianjia.com/ershoufang/gulou/',
	     'https://nj.lianjia.com/ershoufang/jianye/',
	     'https://nj.lianjia.com/ershoufang/qinhuai/',
         'https://nj.lianjia.com/ershoufang/xuanwu/',
	     'https://nj.lianjia.com/ershoufang/yuhuatai/',
	     'https://nj.lianjia.com/ershoufang/qixia/',
	     'https://nj.lianjia.com/ershoufang/jiangning/',
         'https://nj.lianjia.com/ershoufang/pukou/',
         'https://nj.lianjia.com/ershoufang/liuhe/',
	     'https://nj.lianjia.com/ershoufang/lishui/'
    ]

    def parse(self, response):
        area_href = response.url
        for i in range(1, 4):
            try:
                for n in range(1, 60):
                    try:
                        page_url = area_href + 'pg' + str(n) + 'lc' + str(i) + '/'
                        yield scrapy.Request(page_url, callback=self.get_house_url, dont_filter=True)
                    except:
                        break
            except:
                pass

    def get_house_url(self, response):
        print(response.url)
        data = response.body
        soup = BeautifulSoup(data, 'lxml')
        lis = soup.find('div', attrs={'class': 'content '}).find('ul', attrs={'class': 'sellListContent'}).find_all('li',attrs={'class':'clear'})
        for li in lis:
            page_url  = li.find('div', attrs={'class': 'title'}).find('a')['href']
            yield scrapy.Request(page_url, callback=self.get_house_info, dont_filter=True)

    def get_house_info(self,response):
        print('-------------------------------------------------------------------------')
        print(response.url)
        data = response.body
        soup = BeautifulSoup(data,'lxml')
        item = LianjiaItem()
        # 标题部分
        lis1 = soup.find('div', attrs={'class': 'sellDetailHeader'})
        item['title'] = lis1.find('h1')['title']
        item['jianjie'] = lis1.find('div', attrs={'class': 'sub'})['title']
        item['guanzhurenshu'] = lis1.find('span', attrs={'class': 'count', 'id': 'favCount'}).getText()
        item['shoucangrenshu'] = lis1.find('span', attrs={'class': 'count', 'id': 'cartCount'}).getText()
        item['link'] = response.url
        # 基本属性部分
        try:
            lis2 = soup.find('div', attrs={'class': 'base'}).find_all('li')
            item['fangwuhuxing'] = lis2[0].getText().strip('房屋户型').strip()
            item['houseFloor'] = lis2[1].getText().strip('所在楼层').strip()
            item['jianzhumianji'] = lis2[2].getText().strip('建筑面积').strip()
            item['huxingjiegou'] = lis2[3].getText().strip('户型结构').strip()
            item['taoneimianji'] = lis2[4].getText().strip('套内面积').strip()
            item['buildingType'] = lis2[5].getText().strip('建筑类型').strip()
            item['houseOrientation'] = lis2[6].getText().strip('房屋朝向').strip()
            item['jianzhujiegou'] = lis2[7].getText().strip('建筑结构').strip()
            item['Decoration'] = lis2[8].getText().strip('装修情况').strip()
            item['tihubili'] = lis2[9].getText().strip('梯户比例').strip()
            item['ladder'] = lis2[10].getText().strip('配备电梯').strip()
            item['chanquannianxian'] = lis2[11].getText().strip('产权年限').strip()
        except:
            item['fangwuhuxing'] = 'NA'
            item['houseFloor'] = 'NA'
            item['jianzhumianji'] = 'NA'
            item['huxingjiegou'] = 'NA'
            item['taoneimianji'] = 'NA'
            item['buildingType'] = 'NA'
            item['houseOrientation'] = 'NA'
            item['jianzhujiegou'] = 'NA'
            item['Decoration'] = 'NA'
            item['tihubili'] = 'NA'
            item['ladder'] = 'NA'
            item['chanquannianxian'] = 'NA'
        # 交易属性部分
        try:
            lis3 = soup.find('div', attrs={'class': 'transaction'}).find_all('li')
            item['gaipaidata'] = lis3[0].getText().strip('挂牌时间\n').strip()
            item['jiaoyidata'] = lis3[1].getText().strip('交易权属\n').strip()
            item['lastjiaoyidata'] = lis3[2].getText().strip('上次交易\n').strip()
            item['fangwuyongtu'] = lis3[3].getText().strip('房屋用途\n').strip()
            item['fangwunianxian'] = lis3[4].getText().strip('房屋年限\n').strip()
            item['chanquansuoshu'] = lis3[5].getText().strip('产权所属\n').strip()
            item['diyaxinxi'] = lis3[6].getText().strip('抵押信息\n').strip()
            item['fangbenbeijian'] = lis3[7].getText().strip('房本备件\n').strip()
        except:
            item['gaipaidata'] = 'NA'
            item['jiaoyidata'] = 'NA'
            item['lastjiaoyidata'] = 'NA'
            item['fangwuyongtu'] = 'NA'
            item['fangwunianxian'] = 'NA'
            item['chanquansuoshu'] = 'NA'
            item['diyaxinxi'] = 'NA'
            item['fangbenbeijian'] = 'NA'
        # 售房信息部分
        try:
            lis4 = soup.find('div', attrs={'class': 'overview'})
            item['totleprice'] = lis4.find('div', attrs={'class': 'price'}).find('span',attrs={'class': 'total'}).getText()
            item['meanprice'] = lis4.find('div', attrs={'class': 'price'}).find('div',attrs={'class': 'unitPrice'}).getText()
            item['taxprice'] = lis4.find('div', attrs={'class': 'price'}).find('div', attrs={'class': 'tax'}).getText()
            item['houseData'] = lis4.find('div', attrs={'class': 'area'}).find('div',attrs={'class': 'subInfo'}).getText()
            item['xiaoquname'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={'class': 'communityName'}).getText().strip('小区名称').strip('地图')
            item['suozaiarea'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={'class': 'areaName'}).getText().strip('所在区域').strip().replace('\xa0', '-')
            item['kanfangdata'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={'class': 'visitTime'}).getText().strip('看房时间').strip()
            item['lianjiabianhao'] = lis4.find('div', attrs={'class': 'aroundInfo'}).find('div', attrs={ 'class': 'houseRecord'}).getText().strip('链家编号').strip('举报')
        except:
            item['totleprice'] = 'NA'
            item['meanprice'] = 'NA'
            item['taxprice'] = 'NA'
            item['houseData'] = 'NA'
            item['xiaoquname'] = 'NA'
            item['suozaiarea'] = 'NA'
            item['kanfangdata'] = 'NA'
            item['lianjiabianhao'] = 'NA'
        # 房源特色部分
        try:
            lis5 = soup.find('div', attrs={'class': 'introContent showbasemore'})
            item['fangyuantese'] = lis5.getText().strip().replace('\n', '-')
        except:
            item['fangyuantese'] = 'NA'
        # 房源特色部分
        try:
            lis6 = soup.find('div', attrs={'class': 'layout-wrapper'}).find('div', attrs={'class': 'info'})
            item['huxingfenjian'] = lis6.getText().strip().replace('\n', '-')
        except:
            item['huxingfenjian'] = 'NA'

        yield item







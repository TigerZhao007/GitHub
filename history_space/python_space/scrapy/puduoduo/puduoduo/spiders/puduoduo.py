import scrapy
from puduoduo.items import PuduoduoItem
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

class firstSpider(scrapy.Spider):
    name = "puduoduo"
    allowed_domains = ["www.puduoduo58.com/"]
    maxnum = 34
    start_urls = ['http://www.puduoduo58.com/zhuan/index.html'] +  ['http://www.puduoduo58.com/zhuan/index_%s.html' % (str(num)) for num in
                                                range(2, int(maxnum) + 1)]

    def parse(self, response):
        print('----------------------------------------------------')
        print('正在爬取%s页面链接'%(response.url))
        browser = webdriver.PhantomJS(executable_path="D:/python/phantomjs/bin/phantomjs.exe")
        browser.get(response.url)
        time.sleep(1)
        data = browser.page_source
        soup = BeautifulSoup(data, 'lxml')
        lis = soup.find('div', attrs={'class': 'left3'}).find('div', attrs={'class': 'new3'}).find_all('li')
        for li in lis:
            info_url = 'http://www.puduoduo58.com' + li.find('div',attrs= {'class':'lia'}).find('a')['href']
            print('得到%s链接'%(info_url))
            yield scrapy.Request(info_url, callback=self.get_house_info, dont_filter=True)


    def get_house_info(self,response):
        print('----------------------------------------------------')
        print('正在爬取%s具体信息'%(response.url))
        item = PuduoduoItem()
        browser = webdriver.PhantomJS(executable_path="D:/python/phantomjs/bin/phantomjs.exe")
        browser.get(response.url)
        time.sleep(1)
        data = browser.page_source
        soup = BeautifulSoup(data,'lxml')
        item['link'] = response.url
        try:
            lis2 = soup.find('div', attrs={'class': 'main1'}).find('div', attrs={'class': 'left1b'}).find_all('p')
            item['xinxilaiyuan'] = lis2[0].getText().strip('信息来源').replace(' ', '').replace('：', '')
            item['xinxibiaoti'] = lis2[1].getText().strip('信息标题').replace(' ', '').replace('：', '')
            item['suozaidiqu'] = lis2[2].getText().strip('所在地区').replace(' ', '').replace('：', '')
            item['shangpuleixing'] = lis2[3].getText().strip('商铺类型').replace(' ', '').replace('：', '')
            item['shangpumianji'] = lis2[4].getText().strip('商铺面积').replace(' ', '').replace('：', '')
            item['shangpuzujin'] = lis2[5].getText().strip('商铺租金').replace(' ', '').replace('：', '')
            item['lianxiren'] = lis2[6].getText().replace(' ', '').replace('：', '')
        except:
            item['xinxilaiyuan'] = 'NA'
            item['xinxibiaoti'] = 'NA'
            item['suozaidiqu'] = 'NA'
            item['shangpuleixing'] = 'NA'
            item['shangpumianji'] = 'NA'
            item['shangpuzujin'] = 'NA'
            item['lianxiren'] = 'NA'
        try:
            lis3 = soup.find('div', attrs={'class': 'main1'}).find('div', attrs={'class': 'left1c'}).find_all('tr')
            lis4 = soup.find('div', attrs={'class': 'main1'}).find('div', attrs={'class': 'left1d'})
            lis5 = soup.find('div', attrs={'class': 'main1'}).find('div', attrs={'class': 'left1e'})
            item['zhuanrangfeiyong'] = lis3[0].find_all('td')[3].getText()
            item['shiyingjingying'] = lis3[2].find_all('td')[1].getText()
            item['xiangxidizhi'] = lis3[3].find_all('td')[1].getText()
            item['fabushijian'] = lis3[4].find_all('td')[1].getText()
            item['liulancishu'] = lis3[4].find_all('td')[3].getText()
            item['xiangxixinxi'] = lis4.find_all('p')[2].getText()
            item['fangyuantupian'] = lis5.find('div', attrs={'class': 'left1e_b'}).find_all('p')[0].find('img')['src']
        except:
            item['zhuanrangfeiyong'] = 'NA'
            item['shiyingjingying'] = 'NA'
            item['xiangxidizhi'] = 'NA'
            item['fabushijian'] = 'NA'
            item['liulancishu'] = 'NA'
            item['xiangxixinxi'] = 'NA'
            item['fangyuantupian'] = 'NA'
        # print(item)
        print('得到%s信息'%(item['link']))
        yield item


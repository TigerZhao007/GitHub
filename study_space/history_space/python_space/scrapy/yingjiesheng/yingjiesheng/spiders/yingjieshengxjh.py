# -*- coding: utf-8 -*-
import scrapy
from yingjiesheng.items import  YingjieshengItem
import requests
from bs4 import BeautifulSoup

class YingjieshengxjhSpider(scrapy.Spider):
    name = 'yingjieshengxjh'
    allowed_domains = ['yingjiesheng.com/']
    start_urls = ['http://my.yingjiesheng.com/index.php/personal/xjhinfo.htm/?page=1&cid=&city=0&word=&province=0&schoolid=&sdate=&hyid=0']

    def parse(self, response):
        print('正在爬取%s页'%(response.url))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        resq = requests.get(response.url, headers).content
        soup = BeautifulSoup(resq, 'lxml')
        xjh_list = soup.find('div', attrs={'class': 'campus campus-detail campus-h'}).find_all('tr')
        for lis in xjh_list:
            xjh_item = YingjieshengItem()
            try:
                xjh_item['city'] = lis.find('td', attrs={'align': 'center', 'width': '80'}).text.strip()
                xjh_item['date'] = lis.find('td', attrs={'align': 'center', 'width': '120'}).text.strip()
                xjh_item['time'] = lis.find('td', attrs={'align': 'center', 'width': '100'}).find('img')['src'].strip()
                xjh_item['company'] = lis.find('a', attrs={'class': 'f14'}).text.strip()
                xjh_item['school'] = lis.find_all('td', attrs={'width': '250'})[1].text.strip()
                xjh_item['area'] = lis.find('td', attrs={'width': '270'}).text.strip()
                xjh_item['city_link'] = 'http://my.yingjiesheng.com' + \
                                        lis.find('td', attrs={'align': 'center', 'width': '80'}).find('a')['href']
                xjh_item['company_link'] = lis.find('td', attrs={'width': '250'}).find('a')['href']
                xjh_item['school_link'] = 'http://my.yingjiesheng.com' + \
                                          lis.find_all('td', attrs={'width': '250'})[1].find('a')['href']
                xjh_item['detail_link'] = lis.find_all('a')[3]['href']
            except:
                xjh_item['city'] = 'NA'
                xjh_item['date'] = 'NA'
                xjh_item['time'] = 'NA'
                xjh_item['company'] = 'NA'
                xjh_item['school'] = 'NA'
                xjh_item['area'] = 'NA'
                xjh_item['city_link'] = 'NA'
                xjh_item['company_link'] = 'NA'
                xjh_item['school_link'] = 'NA'
                xjh_item['detail_link'] = 'NA'
            yield xjh_item

        # 解析下一页规则，取得后页的xpath
        next_link = soup.find('div', attrs={'class': 'rows page'}).find('a', attrs={'alt': '下页'})['href']
        # 判断是否存在下一页
        if next_link:
            # 如果存在，取得下一页链接，创建回调函数，传递给parse
            next_link = 'http://my.yingjiesheng.com' + \
                        soup.find('div', attrs={'class': 'rows page'}).find('a', attrs={'alt': '下页'})['href']
            yield scrapy.Request(next_link, callback=self.parse, dont_filter=True)



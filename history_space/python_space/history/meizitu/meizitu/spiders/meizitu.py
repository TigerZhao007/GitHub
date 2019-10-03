import scrapy
from meizitu.items import MeizituItem
from bs4 import BeautifulSoup
import requests
from lxml import etree
import time
import os


class firstSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["www.mzitu.com/"]
    start_urls = [
         'http://www.mzitu.com/',
    ]

    def parse(self, response):
        area_href = response.url
        maxnum = 180
        url_list = ['http://www.mzitu.com/'] +  ['http://www.mzitu.com/page/%s/' % (str(num)) for num in
                                                range(2, int(maxnum) + 1)]
        for page_url in url_list:
            yield scrapy.Request(page_url, callback=self.get_pic_url,dont_filter = True)

    def get_pic_url(self,response):
        print('----------------------------------------------------')
        print(response.url)
        item = MeizituItem()
        data = requests.get(response.url).content
        soup = BeautifulSoup(data,'lxml')
        try:
            lis1 = soup.find('div', attrs={'class': 'main'}).find('ul', attrs={'id': 'pins'}).find_all('li')
        except:
            lis1 = []
        for lis in lis1:
            try:
                item['link'] = lis.find('a')['href'].strip(' ')
                item['name'] = lis.find('img')['alt'].strip(' ').replace("!", '').replace("！", '').replace(",",'').replace( "，", '').replace(" ", '').replace(" ", '').replace("？", '').replace("\"", '')
                item['date'] = lis.find_all('span')[1].getText().strip('发布').strip(' ')
                item['data'] = lis.find_all('span')[2].getText().strip('浏览(').strip(')').strip('次').strip(' ')
             #   yield scrapy.Request(url=item['link'], meta={'item': item }, callback=self.get_pic_info )
            except:
                print('加载失败')
            yield item

    # def get_pic_info(self,response):
    #     print('---------------------------------------------------')
    #     print(response.url)
    #     html = requests.get(response.url).content
    #     selector = etree.HTML(html)
    #     maxnum = selector.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()')[0]
    #     url_list = ['%s/%s' % (response.url, str(num)) for num in range(1, int(maxnum) + 1)]
    #     for url2 in url_list:
    #         item = response.meta['item']
    #         selector = requests.get(url2).content
    #         time.sleep(1)
    #         item['pic_link'] =  selector.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src')
    #         yield  item








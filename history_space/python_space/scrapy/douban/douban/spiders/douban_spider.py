# -*- coding: utf-8 -*-
import scrapy
from douban.items import  DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    # 这里是爬虫名
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口URL，传递给调度器里面去,传递给parse
    start_urls = ['https://movie.douban.com/top250']

    # 默认解析方法
    def parse(self, response):
        #循环电影的条目
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i in movie_list:
            # 导入item文件
            douban_item = DoubanItem()
            # 写详细的xpath，进行数据解析
            douban_item['serial_number'] = i.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = i.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = i.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            # 数据的处理
            for j in content:
                content_s = "".join(j.split())
                douban_item['introduce'] = content_s
            douban_item['star'] = i.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = i.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            douban_item['describtion'] = i.xpath(".//p[@class='quote']/span/text()").extract_first()
            # print(douban_item)
            # 你需将数据yield到pipelines中
            yield douban_item
        #解析下一页规则，取得后页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        # 判断是否存在下一页
        if next_link:
            # 如果存在，取得下一页链接，创建回调函数，传递给parse
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)




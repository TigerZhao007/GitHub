
# python爬虫-scrapy教程
创建SCRAPY 爬虫文件编写，编写spider文件，并保存到csv.json.mysql中

# 一、修改工作路径
```python
#在Terminal操作窗口（类似cmd命令行）
cd F:/pythonspace/scrapy
cd
```
# 二、新建一个Scrapy文件
```python
scrapy startproject douban
```
# 三、新建一个Spiders文件
```python
#在Terminal操作窗口（类似cmd命令行
cd douban/douban/spiders #进入spiders文件夹下
scrapy genspider douban_spider movie.douban.com
```
# 四、明确目标，编写items文件
```python
import scrapy
class DoubanItem(scrapy.Item):
    serial_number = scrapy.Field()    # 序号
    movie_name = scrapy.Field()    # 电影名称
    introduce = scrapy.Field()    # 简介
    star = scrapy.Field()    # 明星
    evaluate = scrapy.Field()    # 评价
    describtion = scrapy.Field()    # 描述
# 注意取名字时不要取敏感单词，函数单词等
```
# 五、爬虫文件编写，编写spider文件
```python
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
```
# 六、修改settings文件
```python
DOWNLOAD_DELAY = 0.5    # 下载延迟修改成0.5秒
ROBOTSTXT_OBEY = False  # 修改成F
LOG_FILE = "scrapy.log" # 添加这行字段
USER_AGENT  = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' # 修改USER_AGENT文件
```
# 七、代码运行测试
```python
#在Terminal操作窗口（类似cmd命令行）
cd douban/ #进入douban文件夹下
scrapy crawl douban_spider
```
# 八、新建main.py文件
```python
# from scrapy import cmdline
# cmdline.execute('scrapy crawl douban_spider'.split())
# 运行报错，但是在cmd&pythonconsole运行正常，问题待解决。。。。。。。。。。。。。。。。。。。。
```

# 九、保存到CSV、Json文件中
```python
#在Terminal操作窗口（类似cmd命令行）
cd douban/ #进入希望保存数据的文件夹下
scrapy crawl douban_spider -o test.csv    # 直接Excel打开乱码，先用notepad++修改成UTF-8bom，后用Excel打开即可，数据存储较乱
scrapy crawl douban_spider -o test.json  # 保存为json文件看，二进制格式
```

# 十、保存到数据库中
### 首先，修改settings文件
```python
ITEM_PIPELINES = {
    'douban.pipelines.DoubanPipeline': 300,
}
```
### 其次，编写pipelines文件
```python
import pymysql.cursors
import pymysql

class DoubanPipeline(object):
    # douban_item为spider传递过来的名字。
    def process_item(self, douban_item, spider):
        # 链接数据库
        conn = pymysql.connect(host='127.0.0.1',
                               user = 'root',
                               password = 's3438838',
                               db = 'test',
                               charset="utf8")
        cur = conn.cursor()

        # 创建数据库代码
        sql1 = """CREATE TABLE IF NOT EXISTS test2(
                serial_number text, movie_name text,
                star text,     introduce text,
                evaluate text, describtion text)
                 """
        # 执行创建数据库
        cur.execute(sql1)

        # 上传数据库代码
        sql2 = """INSERT INTO test2(serial_number,movie_name,star,introduce,evaluate,describtion) value
        (%s,%s,%s,%s,%s,%s)"""
        # 上次数据库数据
        lis = (douban_item['serial_number'],douban_item['movie_name'],douban_item['star'],douban_item['introduce'],
               douban_item['evaluate'], douban_item['describtion'])
        # 执行上传数据库
        cur.execute(sql2, lis)

        # 打印保存数据进度
        print('成功保存编号%s房源'%(douban_item['serial_number']))
        # 提交数据
        conn.commit()

        # 关闭数据库链接
        cur.close()
        conn.close()

        return douban_item
```
# 十一、设置代理IP
首先，编写middlewares文件
```python
class my_proxy(object):
    def process_request(self, request,spider):
        request.meta['proxy'] = 'http-cla.abyun.com:9030'
        proxy_name_pass = b'H211EATS905745KC:F8FFBC929EB7D5A7'
        encode_pass_name = base64.b64encode(proxy_name_pass)
        request.headers['Proxyy-Autorization'] = 'Basic ' + encode_pass_name.decode()
```
### 其次，修改settings文件
```python
DOWNLOADER_MIDDLEWARES = {
    'douban.middlewares.my_proxy': 543,
}
```
# 十二、设置随机UserAgent
### 首先，编写middlewares文件
```python
class my_useragent(object):
    def process_request(self, request,spider):
        agents = [
            "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14"
        ]
        agent = random.choice(agents)
        request.headers['User_Agent'] = agent
```
### 其次，修改settings文件
```python
DOWNLOADER_MIDDLEWARES = {
    'douban.middlewares.my_proxy': 543,
    'douban.middlewares.my_useragent': 544,
}
```





# selenimu爬虫教程

# 加载模块
```buildoutcfg
from bs4 import BeautifulSoup
from selenium import webdriver  
```

# 设置初始URL和headers
```buildoutcfg
url = 'http://my.yingjiesheng.com/index.php/personal/xjhinfo.htm/?page=1&cid=&city=0&word=&province=0&schoolid=&sdate=&hyid=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
```

```buildoutcfg
browser = webdriver.PhantomJS(executable_path="D:/python/phantomjs/bin/phantomjs.exe")
browser.get(url)
data = browser.page_source
soup = BeautifulSoup(data, 'lxml')
lis = soup.find('div', attrs={'class': 'left3'}).find('div', attrs={'class': 'new3'}).find_all('li')
```

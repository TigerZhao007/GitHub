# Requests爬虫教程

# 一、常用操作
##  1.加载相关模块
```buildoutcfg
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

## 2.设置初始URL和headers
```buildoutcfg
url = 'http://my.yingjiesheng.com/index.php/personal/xjhinfo.htm/?page=1&cid=&city=0&word=&province=0&schoolid=&sdate=&hyid=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
```

## 3.获取网页源代码并解析
```buildoutcfg
resq = requests.get(url,headers).content
soup = BeautifulSoup(resq, 'lxml')
lis = soup.find('div',attrs={'class':'campus campus-detail campus-h'}).find_all('tr')
```

# 二、教程
原文链接：https://www.cnblogs.com/lei0213/p/6957508.html

## 1.返回结果
```buildoutcfg
import requests 
response  = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
print(type(response.text)) 
response.enconding = "utf-8'
print(response.text) 
print(response.cookies) 
print(response.content)
print(response.content.decode("utf-8"))
```
response.text返回的是Unicode格式，通常需要转换为utf-8格式，否则就是乱码。response.content是二进制模式，
可以下载视频之类的，如果想看的话需要decode成utf-8格式。<br>
不管是通过response.content.decode("utf-8)的方式还是通过response.encoding="utf-8"的方式
都可以避免乱码的问题发生<br>

## 2.一大推请求方式
```buildoutcfg
import requests
requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")
```
## 3.基本GET
```buildoutcfg
import requests 
url = 'https://www.baidu.com/'
response = requests.get(url)
print(response.text)
```
* 带参数的GET请求：<br>
如果想查询http://httpbin.org/get页面的具体参数，需要在url里面加上，
例如我想看有没有Host=httpbin.org这条数据，url形式应该是http://httpbin.org/get?Host=httpbin.org<br>
下面提交的数据是往这个地址传送data里面的数据。<br>
```buildoutcfg
import requests 
url = 'http://httpbin.org/get'
data = {
    'name':'zhangsan',
    'age':'25'
}
response = requests.get(url,params=data)
print(response.url)
print(response.text)
```
* Json数据：<br>
从下面的数据中我们可以得出，如果结果：<br>
1、requests中response.json()方法等同于json.loads（response.text）方法<br>
```buildoutcfg
import requests
import json 
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json())
```
* 获取二进制数据<br>
在上面提到了response.content，这样获取的数据是二进制数据，同样的这个方法也可以用于下载图片以及视频资源

* 添加header<br>
首先说，为什么要加header（头部信息）呢？<br>
例如下面，我们试图访问知乎的登录页面（当然大家都你要是不登录知乎，就看不到里面的内容），
我们试试不加header信息会报什么错。<br>
结果：提示发生内部服务器错误（也就说你连知乎登录页面的html都下载不下来）。如果想访问就必须得加headers信息。<br>
```buildoutcfg
import requests 
url = 'https://www.zhihu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
response = requests.get(url,headers=headers)
print(response.text)
```
## 4.基本post请求
通过post把数据提交到url地址，等同于一字典的形式提交form表单里面的数据<br>
```buildoutcfg
import requests 
url = 'http://httpbin.org/post'
data = {
    'name':'jack',
    'age':'23'
    }
response = requests.post(url,data=data)
print(response.text)
```
响应：<br>
```buildoutcfg
import requests
 
response = requests.get("http://www.baidu.com")         
# 打印请求页面的状态（状态码）
print(type(response.status_code),response.status_code)   
# 打印请求网址的headers所有信息
print(type(response.headers),response.headers)       
# 打印请求网址的cookies信息
print(type(response.cookies),response.cookies)     
# 打印请求网址的地址
print(type(response.url),response.url)     
# 打印请求的历史记录（以列表的形式显示）
print(type(response.history),response.history)  
```
内置的状态码：<br>
```buildoutcfg
import requests
response = requests.get('http://www.jianshu.com/404.html')
# 使用request内置的字母判断状态码 
# 如果response返回的状态码是非正常的就返回404错误
if response.status_code != requests.codes.ok:
    print('404') 
# 如果页面返回的状态码是200，就打印下面的状态
response = requests.get('http://www.jianshu.com')
if response.status_code == 200:
    print('200')
```
# 三、request的高级操作
## 1.文件上传
```buildoutcfg
import requests
url = "http://httpbin.org/post"
files= {"files":open("test.jpg","rb")}
response = requests.post(url,files=files)
print(response.text)
```
## 2.获取cookie
```buildoutcfg
import requests
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key,value in response.cookies.items():
    print(key,'==',value)
```
## 3.会话维持
cookie的一个作用就是可以用于模拟登陆，做会话维持
```buildoutcfg
import requests
session = requests.session()
session.get('http://httpbin.org/cookies/set/number/12456')
response = session.get('http://httpbin.org/cookies')
print(response.text)
```
## 4.证书验证
* 无证书访问
```buildoutcfg
import requests
response = requests.get('https://www.12306.cn')
# 在请求https时，request会进行证书的验证，如果验证失败则会抛出异常
print(response.status_code)
```
* 关闭证书验证
```buildoutcfg
import requests
# 关闭验证，但是仍然会报出证书警告
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
```
为了避免这种情况的发生可以通过verify=False，但是这样是可以访问到页面结果
* 消除验证证书的警报
```buildoutcfg
from requests.packages import urllib3
import requests 
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
```
## 5.手动设置证书
```buildoutcfg
import requests 
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)
```
## 6.代理设置
1、设置普通代理
```buildoutcfg
import requests 
proxies = {
  "http": "http://127.0.0.1:9743",
  "https": "https://127.0.0.1:9743",
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)
```
2、设置用户名和密码代理
```buildoutcfg
import requests 
proxies = {
    "http": "http://user:password@127.0.0.1:9743/",
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)
```
## 7.设置socks代理
全能代理，就像有很多跳线的转接板，它只是简单地将一端的系统连接到另外一端。<br>
支持多种协议，包括http、ftp请求及其它类型的请求。它分socks 4 和socks 5两种类型.<br>
socks 4只支持TCP协议而socks 5支持TCP/UDP协议，还支持各种身份验证机制等协议。其标准端口为1080。<br>
在实际应用中SOCKS代理可以用作为：电子邮件、新闻组软件、网络传呼ICQ、网络聊天MIRC和使用代理服务器打游戏等等各种应用软件当中。
```buildoutcfg
# 安装socks模块 pip3 install 'requests[socks]'
import requests 
proxies = {
    'http': 'socks5://127.0.0.1:9742',
    'https': 'socks5://127.0.0.1:9742'
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)
```
## 8.超时设置
* 通过timeout参数可以设置超时的时间<br>
```buildoutcfg
import requests
from requests.exceptions import ReadTimeout 
try:
    # 设置必须在500ms内收到响应，不然或抛出ReadTimeout异常
    response = requests.get("http://httpbin.org/get", timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
```
* 认证设置<br>
如果碰到需要认证的网站可以通过requests.auth模块实现  <br>
```buildoutcfg
import requests
from requests.auth import HTTPBasicAuth
<br>#方法一
r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))<br>
#方法二<br>r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
print(r.status_code)
```
* 异常处理<br>
关于reqeusts的异常在这里可以看到详细内容：<br>
http://www.python-requests.org/en/master/api/#exceptions<br>
所有的异常都是在requests.excepitons中,从源码我们可以看出:<br>
```buildoutcfg
RequestException继承IOError,
HTTPError，ConnectionError，Timeout继承RequestionException,
ProxyError，SSLError继承ConnectionError,
ReadTimeout继承Timeout异常.
```
这里列举了一些常用的异常继承关系，详细的可以看：<br>
http://cn.python-requests.org/zh_CN/latest/_modules/requests/exceptions.html#RequestException<br>
通过下面的例子进行简单的演示:<br>
```buildoutcfg
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
try:
    response = requests.get("http://httpbin.org/get", timeout = 0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection error')
except RequestException:
    print('Error')
```
首先被捕捉的异常是timeout,当把网络断掉的haul就会捕捉到ConnectionError，
如果前面异常都没有捕捉到，最后也可以通过RequestExctption捕捉到
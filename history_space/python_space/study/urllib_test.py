import urllib.request
# import cookielib

url = "http://maoyan.com/board/4"

print('第一种方法')
resp1 = urllib.request.urlopen(url)
print(resp1.getcode())
print(len(resp1.read()))

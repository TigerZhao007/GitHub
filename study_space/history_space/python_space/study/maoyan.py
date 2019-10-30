import requests

url = 'http://maoyan.com/board/4?offset=10'
url = 'http://maoyan.com/board/4'
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

req = requests.get(url, headers = headers)
print(req.content)
print(req.text)
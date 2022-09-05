import requests

url = 'http://www.baidu.com/s'

param = {"id": 1001, 'wd': 101}

r = requests.get(url, params=param)

print('url: ', r.url)
print('status: ', r.status_code)
# print('text: ', r.text)
print('encoding: ', r.encoding)
print('headers: ', r.headers)
print('cookies: ', r.cookies)

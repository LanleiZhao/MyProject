# -*- coding:utf-8 -*-
import requests

# url = "http://www.baidu.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
# p = {"wd":"百度"}
# response = requests.get(url,headers=headers,params=p)
# print(response.status_code)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
url = "http://www.baidu.com/s?wd={}".format('人工智能')

response = requests.get(url,headers=headers)
print(response.status_code)


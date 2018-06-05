#coding:utf-8
import requests
from bs4 import BeautifulSoup

res = requests.get('https://mil.news.sina.com.cn/')
res.encoding = 'utf-8'
print(res.text)

#一定要搞定你 草死
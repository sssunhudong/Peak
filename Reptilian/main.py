#coding:utf-8
import requests #网络资源获取套件

from bs4 import BeautifulSoup

res = requests.get('https://mil.news.sina.com.cn/')
res.encoding = 'utf-8'
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
head = soup.select('a') #select 用于筛选出含有此标签的元素
# 找出所有id为title的元素id前面需加#号 soup.select('#title')
# 找出所有class为link的元素前面加.号 soup.select('.link')
#print(type(head))

#for h in head :
   # print(h.text) #打印出包含的文字

print(head[0]['class']) #打印出此标签的内容 head为列表，如果有次标签，没有的话报错
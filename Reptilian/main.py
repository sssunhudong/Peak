#coding:utf-8
import requests #网络资源获取套件
from datetime import datetime
from bs4 import BeautifulSoup

# res = requests.get('https://mil.news.sina.com.cn/')
# res.encoding = 'utf-8'
# #print(res.text)
#
# soup = BeautifulSoup(res.text, 'html.parser')
# head = soup.select('a') #select 用于筛选出含有此标签的元素
# 找出所有id为title的元素id前面需加#号 soup.select('#title')
# 找出所有class为link的元素前面加.号 soup.select('.link')
#print(type(head))

# for h in head :
#     print(h['href'])
#     print(h.text) #打印出包含的文字

#print(head[0]['class']) #打印出此标签的内容 head为列表，如果有次标签，没有的话报错

#抓取新闻内容
res = requests.get('http://mil.news.sina.com.cn/china/2018-06-05/doc-ihcmurvi0652801.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.select('.main-title')[0].text)
print(soup.select('.date-source')[0].text)
print('--------------------------')
print(soup.select('.date-source span')[0].text)#用空格抽取该条目下的分类数据
print('--------------------------')
print(soup.select('.date-source a')[0].text)
print('--------------------------')

myText = []
doc = soup.select('#article p')[1:]
for t in doc:
    #print(t.text)
    myText.append(t.text.strip())#strip()去除空格符号 可以填写具体要移除的内容
print('\n'.join(myText))#用指定符号将列表合并
print('--------------------------')
#简化
#print('\n'.join([t.text.strip() for t in doc]))

print('--------------------------')

#评论

comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=jc&newsid=comos-hcmurvi0652801&'
                        'group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&'
                        'thread=1&callback=jsonp_1528268044120&_=1528268044120')
# str = []
# str.append(comments.text.strip('jsonp_1528268044120(').strip(')'))

#print(str)
import json
import pandas

jd = json.loads(comments.text.strip('jsonp_1528268044120(').strip(')'))
print(jd['result']['count']['total'])#获取了评论数目
#字符串转时间
timesource = soup.select('.date')[0].text
dt = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
print(dt)
print('--------------------------')
#时间转字符串

print(dt.strftime('%Y-%m-%d'))
print('--------------------------')
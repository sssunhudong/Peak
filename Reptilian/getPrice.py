#coding:utf-8
import requests
from bs4 import BeautifulSoup
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import re
#筛选商品网城类型
def checkUrlType(url):
    type = -1
    if(re.search('detail.tmall', url)):
        type = 1
    elif(re.search('item.taobao', url)):
        type = 2
    elif(re.search('item.jd', url)):
        type = 3
    return type

# def getFlag(type):
#     str = ''
#     if(1 == type)
#         str = 'tm-price'
#     elif(2 == type)
#         str = 'tb-rmb-num'
#     elif(3 == type)
#         str =
#     return str

def getPrice(url):
    price = 0
    type = checkUrlType(url)
    #区分用户输入网址的类型：根据类型抓取不同的价格参数
    # 1=天猫https://detail.tmall.com，<span class="tm-price">59.00</span>
    # 2=淘宝https://item.taobao.com，<em id="J_PromoPriceNum" class="tb-rmb-num">49.00</em>
    # 3=京东https://item.jd.com <span class="price J-p-198626">99.00</span> (J-p-198626数字从网址尾部取)
    return price

# res = requests.get('https://s.taobao.com/search?q=纸尿裤&s=0')
# res.encoding = 'utf-8'
# print(res.apparent_encoding)#自动获取编码

# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
browser = webdriver.Chrome()
webdriver.PhantomJS
# browser.maximize_window()
# browser.get('https://detail.tmall.com/item.htm?id=40348345632&ali_refid=a3_430583_1006:1109725094:'
#             'N:%E7%82%8A%E5%A4%A7%E7%9A%87%20%E5%A5%B6%E9%94%85:318333211bd1ce718705998f72171618&al'
#             'i_trackid=1_318333211bd1ce718705998f72171618&spm=a230r.1.14.1')
# assert"Python"in browser.title
# elem = browser.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
#print(browser.page_source)



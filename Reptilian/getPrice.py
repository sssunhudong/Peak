#coding:utf-8
import requests
from bs4 import BeautifulSoup
import math
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

res = requests.get('https://detail.tmall.com/item.htm?id=40348345632&ali_refid=a3_430583_1006:1109725094:N:%E5%A5%B6%E9%94%85:c6a7545ba26284bbfa16948da6d31004&ali_trackid=1_c6a7545ba26284bbfa16948da6d31004&spm=a230r.1.14.1&skuId=3658350814878')
res.encoding = 'utf-8'
print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# head = soup.select('.tb-meta')
# print(head)
#coding:utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
#打开浏览器模式
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# assert u"百度" in driver.title
# elem = driver.find_element_by_name("wd")
# elem.clear()
# elem.send_keys(u"网络爬虫")
# elem.send_keys(Keys.RETURN)
# time.sleep(3)
# assert u"网络爬虫." not in driver.page_source
# driver.close()

#无浏览器模式 但最新的不支持了，要使用浏览器的无界面模式
# driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# driver.get("https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.12b37dccOwQJO9&id=557575103895&skuId=3669811590228&user_id=2541050533&cat_id=50069259&is_b=1&rn=cf90cfd6e0f69afafacb7436001867c9")
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

#无界面模式
options = webdriver.ChromeOptions()
options.set_headless()
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options = options)
driver.get("https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.12b37dccOwQJO9&id=557575103895&skuId=3669811590228&user_id=2541050533&cat_id=50069259&is_b=1&rn=cf90cfd6e0f69afafacb7436001867c9")
print(driver.page_source)


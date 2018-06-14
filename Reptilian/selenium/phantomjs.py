#coding:utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
#打开浏览器模式
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.taobao.com/")
#断言检查
assert u"淘宝" in driver.title
elem = driver.find_element_by_class_name('search-combobox-input')
elem.clear()
elem.send_keys(u"奶锅")
#elem.send_keys(Keys.RETURN)
#找到按钮模拟鼠标点击
# from selenium.webdriver.common.by import By
# click = driver.find_element(By.CLASS_NAME, 'search-button')#这是通用方法 寻找一个，elements是寻找多个，下同
click = driver.find_element_by_class_name('search-button')
click.click()
time.sleep(3)
#assert u"网络爬虫." not in driver.page_source
driver.close()

#无浏览器模式 但最新的不支持了，要使用浏览器的无界面模式
# driver = webdriver.PhantomJS(executable_path=r'F:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# driver.get("https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.12b37dccOwQJO9&id=557575103895&skuId=3669811590228&user_id=2541050533&cat_id=50069259&is_b=1&rn=cf90cfd6e0f69afafacb7436001867c9")
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

#无界面模式
# options = webdriver.ChromeOptions()
# options.set_headless()
# options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(options = options)
# #driver.get("https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.12b37dccOwQJO9&id=557575103895&skuId=3669811590228&user_id=2541050533&cat_id=50069259&is_b=1&rn=cf90cfd6e0f69afafacb7436001867c9")
# driver.get("https://www.baidu.com")
# print(driver.page_source)


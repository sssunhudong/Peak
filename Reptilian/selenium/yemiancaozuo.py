#coding:utf-8

__author__ = 'hudong'

from selenium import webdriver
from time import sleep
from urllib import request



# #窗口的切换
# # driver = webdriver.Chrome()
# # driver.get("file:// /f:/login.html")
# # sleep(1)
# # #新的窗口打开
# # js = 'window.open("http://www.baidu.com");'
# # driver.execute_script(js)
# # js = 'window.open("http://www.taobao.com");'
# # driver.execute_script(js)
# # js = 'window.open("http://www.jd.com");'
# # driver.execute_script(js)
# # #获取当前窗口句柄(file:// /f:/login.html)
# # cur = driver.current_window_handle
# # driver.close()
# # #获取所有窗口句柄列表 注意顺序第一次打开的是0，之后顺序为逆序最后一次打开的是1
# # handles = driver.window_handles
# #遍历句柄
# for handle in handles:
#         driver.switch_to.window(handle)
#         sleep(2)
# driver.close()


#切换页面frame
driver = webdriver.Chrome()
driver.get("http://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols")
#定位父类层级iframe
ele_framest = driver.find_element_by_css_selector("#result > iframe")
#切换到父类层级
driver.switch_to.frame(ele_framest)
print(driver.page_source)
print("____________________________________")

#切换到第二个子类frame switch_to貌似不支持索引
driver.switch_to_frame(1)
print(driver.page_source)
print("____________________________________")

#切换到最上层frame
driver.switch_to.parent_frame()
print(driver.page_source)
print("____________________________________")



#下拉列表的选择 有三种选择方式 如果下索引 文字 value值
# from selenium.webdriver.support.ui import Select
# select = Select(driver.find_element_by_xpath('//form/select'))
# time.sleep(5)
# select.select_by_index(1)
# time.sleep(5)
# select.select_by_visible_text(u"邮箱")
# time.sleep(5)
# select.select_by_value('name')
sleep(1)


#元素拖拽代码
# from selenium.webdriver import ActionChains
# element = driver.find_element_by_name("source")
# target = driver.find_element_by_name("target")
# action = ActionChains(driver)
# action.drag_and_drop(element, target).perform()




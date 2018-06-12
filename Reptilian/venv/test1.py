#coding:utf-8

'test1 mode'

__author__ = 'hudong'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        print(driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "NO results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

# t = PythonOrgSearch()
# t.setUp()
# t.test_search_in_python_org()
# t.tearDown()




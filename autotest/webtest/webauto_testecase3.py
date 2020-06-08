# -*- coding: utf-8 -*-
# @Time    : 2020-6-8 20:40  
# @Author  : Administrator
# @FileName: webauto_testecase3.py
# @Software: PyCharm
# !/usr/bin/python


import os
import time
import unittest
import pymysql
import fconfig
from selenium import webdriver
import HTMLTestRunner

PATH=lambda p:os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)
global driver

HOST='127.0.0.1'
class Search(unittest.TestCase):
    """搜索：自动化平台测试开发，软件自动化测试开发"""
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get('http://www.baidu.com')
        time.sleep(1)

    def test_readSQLcase1(self):
        sql='SELECT id,Webfindmethod,Webevelement,weboptmethod,webtestdata,webassertdata,webtestresult FROM webtest_webcasestep where webtest_webcase.Webcase_id=1 ORDER BY id ASC'
        coo=
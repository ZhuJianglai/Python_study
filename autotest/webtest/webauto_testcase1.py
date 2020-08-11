# -*- coding: utf-8 -*-
# @Time    : 2020-8-11 0011 19:06 
# @Author  : 081191 
# @FileName: webauto_testcase1.py                     
# @Software: PyCharm 
# !/usr/bin/python

import time
from selenium import webdriver

if __name__=='__main__':
    global driver
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    time.sleep(1)
    driver.find_element_by_id('kw').send_keys('软件自动化测试')
    time.sleep(1)
    driver.find_element_by_id('su').click()
    driver.quit()
    print('Done')
    time.sleep(1)
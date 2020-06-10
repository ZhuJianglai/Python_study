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
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        time.sleep(1)

    def test_readSQLcase1(self):
        sql='SELECT id,Webfindmethod,Webevelement,weboptmethod,webtestdata,webassertdata,webtestresult FROM webtest_webcasestep where webtest_webcase.Webcase_id=1 ORDER BY id ASC'
        coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host=fconfig.getConfig('database','host'),charset='utf8')
        cursor=coo.cursor()
        aa=cursor.execute(sql)
        info=cursor.fetchmany(aa)
        for ii in info:
            case_list=[]
            case_list.append(ii)
            webtestcase(case_list,self)
        coo.commit()
        cursor.close()
        coo.close()


    def tearDown(self):
        self.driver.quit()



def webtestcase(case_list,self):
    for case in case_list:
        try:
            case_id=case[0]
            findmethod=case[1]
            evelement=case[2]
            optmethod=case[3]
            testdata=case[4]
        except Exception as e:
            return '测试用例格式 不正确%s'%e
        print(case)
        time.sleep(5)
        if optmethod=='sendkeys' and findmethod=='find_element_by_id':
            self.driver.find_element_by_id(evelement).send_keys(testdata)
        elif optmethod=='click' and findmethod=='find_element_by_name':
            print(evelement)
            self.driver.find_element_by_name(evelement).click()
        elif optmethod=='click' and findmethod=='find_element_by_id':
            print(evelement)
            self.driver.find_element_by_id(evelement).click()


if __name__ =='__main__':
    time.sleep(1)
    nowww=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    testunit=unittest.TestSuite()
    testunit.addTest(Search("test_readSQLcase1"))
    testunit.addTest(Search("test_readSQLcase2"))

    filename="webtest_report.html"  #有点不明白
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='web自动化测试报告',description=U'搜索测试用例')
    runner.run(testunit)
    print('Done')
    time.sleep(1)


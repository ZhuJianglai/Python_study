# -*- coding: utf-8 -*-
# @Time    : 2020-8-11 0011 19:41 
# @Author  : 081191 
# @FileName: webauto_testcase2.py                     
# @Software: PyCharm 
# !/usr/bin/python

import os
import time
import unittest
import pymysql
import fconfig
from selenium import webdriver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
global driver

HOSTNAME='127.0.0.1'

def readSQLcase():
    sql="select id,webteststep,webfindmethod,webevelement,weboptmethod,webtestdata,webassertdata,webtestresult from autotest.webtest_webcasestep where autotest.webtest_webcasestep.webcase_id=3 order by id asc"
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host=HOSTNAME,chartset='utf8')
    cursor=coo.cursor()
    aa=cursor.execute(sql)
    info=cursor.fetchmany(aa)
    for ii in info:
        case_list=[]
        case_list.append(ii)
        webtestcase(case_list)
    coo.commit()
    cursor.close()
    coo.close()


def webtestcase(case_list):
    for case in case_list:
        try:
            case_id=case[0]
            findmethod=case[2]
            evelement=case[3]
            optmethod=case[4]
            testdata=case[5]
        except Exception as e:
            return "测试用例格式不正确！%s"%e
        print(case)
        time.sleep(5)
        if optmethod=='sendkeys' and findmethod=='find_element_by_id':
            print(evelement)
            driver.find_element_by_id(evelement).send_keys(testdata)
        elif optmethod=='click' and findmethod=='find_element_by_name':
            print(evelement)
            driver.find_element_by_name(evelement).click()
        elif optmethod=='click' and findmethod=='find_element_by_id':
            print(evelement)
            driver.find_element_by_id(evelement).click()

if __name__=='__main__':
     time.sleep(1)
     global driver
     driver=webdriver.Chrome()
     driver.get('http://www.baidu.com')
     time.sleep(1)
     readSQLcase()
     time.sleep(1)
     driver.quit()

     print('Done')
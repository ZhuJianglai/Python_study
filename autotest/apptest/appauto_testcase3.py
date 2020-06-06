# -*- coding: utf-8 -*-
# @Time    : 2020-6-6 15:27 
# @Author  : 081191 
# @FileName: appauto_testcase3.py                     
# @Software: PyCharm 
# !/usr/bin/python

import os
import time
import unittest
from selenium import webdriver

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
global driver

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['device']='android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']=4.4
        desired_caps['deviceName']='emulator-5554'
        PATH('E:\\')
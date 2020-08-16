# -*- coding: utf-8 -*-
# @Time    : 2020-8-12 22:54  
# @Author  : Administrator
# @FileName: fconfig.py.py
# @Software: PyCharm
# !/usr/bin/python


import configparser
import os

def getConfig(section,key):
    config=configparser.ConfigParser()
    path=os.path.split(os.path.realpath(__file__))[0]+'/settings.ini'
    config.read(path)
    return config.get(section,key)

#
# if __name__=='__main__':
#     print(getConfig('database','host'))


# -*- coding: utf-8 -*-
# @Time    : 2020-6-5 19:51 
# @Author  : 081191 
# @FileName: config.py                     
# @Software: PyCharm 
# !/usr/bin/python


import ConfigParser
import os
def getConfig(section,key):
    config=ConfigParser.ConfigParser()
    path=os.path.split(os.path.realpath(__file__))[0]+'/settings.conf'
    config.read(path)
    return config.get(section,key)
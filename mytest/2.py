# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 16:46
# @Author  : 081191
# @FileName: 2.py
# @Software: PyCharm
# !/usr/bin/python
import datetime
import os


for filename in os.listdir(r'E:\python_study\mytest'):

    # print(filename,os.path.getmtime('E:\OTA\lib_sign\\' + filename))   #输出文件创建时间)
    i = datetime.datetime.now()
    year=i.year
    month=i.month
    day=i.day
    if i.month<10 :
        month=str(0)+str(i.month)
    if i.day<10:
        day=str(0)+str(i.day)
    time_str=str(year)+str(month)+str(day)
    print(filename)
    if time_str in filename:
        print(filename)

    from os import path

    d = path.dirname(__file__)
    print(d)

    # print("当前的日期和时间是 %s" % i)
    # print("ISO格式的日期和时间是 %s" % i.isoformat())
    # print("当前的年份是 %s" % i.year)
    # print("当前的月份是 %s" % i.month)
    # print("当前的日期是  %s" % i.day)
    # print("yyyymmdd 格式是  %s%s%s" % (i.year,i.month,i.day-1))
    # print("当前小时是 %s" % i.hour)
    # print("当前分钟是 %s" % i.minute)
    # print("当前秒是  %s" % i.second)




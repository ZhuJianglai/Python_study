# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 14:30
# @Author  : 081191
# @FileName: file_filter.py
# @Software: PyCharm


import os
import glob
import datetime

#获取昨天的日志

def get_yestoday_log(filepath):
    time_name=(datetime.date.today()+datetime.timedelta(-1)).strftime('%Y%m%d')
    os.chdir(filepath)
    for logname in glob.glob("UartLog_"+time_name+".log"):
        return logname


if __name__ =="__main__":
    path = "E:\OTA\lib_sign"
    print(get_yestoday_log(path))

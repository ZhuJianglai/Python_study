# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 18:29
# @Author  : 081191
# @FileName: listFilename.py
# @Software: PyCharm


import os
import glob
import datetime

def new_report(test_report):
    # lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    # print(lists)
    str_name=(datetime.date.today() + datetime.timedelta(-1)).strftime("%Y%m%d")
    os.chdir(test_report)
    for file in glob.glob("UartLog_"+str_name+".log"):
    # lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn),reverse=True)#按时间排序
        print(file)
    # print(lists)                 #获取最新的文件保存到file_new
    # print(lists[0])
    # return lists[0]
    # print(file_new)
    # return file_new
if __name__=="__main__":
    test_report="E:\OTA\lib_sign"#目录地址
    print(new_report(test_report))
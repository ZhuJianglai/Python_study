# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 13:44
# @Author  : 081191
# @FileName: list_file.py
# @Software: PyCharm
import os
file_path="E:\OTA" #目录地址

# 获取最新的文件
def file_name(file_path):
    lists = os.listdir(file_path)                                    #列出目录的下所有文件和文件夹保存到lists
    # print(lists)
    lists.sort(key=lambda fn:os.path.getmtime(file_path + "\\" + fn),reverse=True)#按时间排序
    # print(lists)
    # file_new = os.path.join(file_path,lists[0])                     #获取最新的文件保存到file_new
    # print(file_new)
    # print(lists[1])
    return lists

# print(file_name(file_path))
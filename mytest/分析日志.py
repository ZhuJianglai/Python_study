# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 11:34
# @Author  : 081191
# @FileName: 分析日志.py
# @Software: PyCharm

str_1="Cmode"
def read_txt_high(filename):
    with open(filename,'r') as file_to_read:
        # list0 = [] #文件中的第一列数据
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if str_1 in lines:
                f = open("input.txt", "a+")
                f.write(lines+'\n')




read_txt_high("UartLog_20190326.log")




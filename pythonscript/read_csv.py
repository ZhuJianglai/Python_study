# -*- coding: utf-8 -*-
# @Time    : 2020-7-13 20:56  
# @Author  : Administrator
# @FileName: read_csv.py
# @Software: PyCharm
# !/usr/bin/python
import csv
import pandas as pd
from datetime import datetime
import time
a=[]
str_off_on={0:'关闭',1:'开',2:'待机'}
str_system_model={0:'无法解析',1:'舒适',2:'厨房',3:'四季感',4:'节能',5:'厨房',6:'厨房',7:'厨房',8:'厨房',9:'厨房',10:'厨房',17:'厨房',18:'厨房',19:'高温水',20:'厨房',21:'厨房',22:'厨房',23:'宝宝洗',24:'儿童洗'}
lls_dic={0:'全天候',1:'点动',2:'点动',3:'单循环',4:'点动',5:'点动',6:'单循环',7:'水增压'}
# [0,1,1,0,10,0,38,27,0,1,0,0,27,0,16,39,0,0,2,34,18,23,0,0,0,0,0,13,12,0,0,0,0,0,0,0]
# title = [U'时间',U'brand', U'category', U'deviceId', U'model', u'series', U'用水累加量',U'用气累加量',U'零冷水模式',U'水增压+',U'点动+',U'单巡航',U'零冷水预约状态模式']  # 表格title
title = [U'Mac',U'开关机', U'模式', U'设置温度', U'零冷水模式', u'名称']  # 表格title
def read_csv():
    with open('E:/python/在线燃热原始数据01.csv', 'r') as f:
         reader = csv.reader(f)
         print(type(reader))

         for row in reader:
            for i in range(row.__len__()):
                if i==0:
                    mac=row[i]
                if i==1:
                    temp_list=eval(row[i])
                    print(type(temp_list))
                    for n in range(temp_list.__len__()):
                        if n==1:
                            off_on=temp_list[n]
                            off_on=str_off_on[off_on]
                            print(off_on)
                        if n==2:
                            system_model=temp_list[n]
                            system_model=str_system_model[system_model]
                        if n==6:
                            szwd=temp_list[n]
                        if n==19:
                            lls=temp_list[n]
                            lls_str=bin(int(lls)).replace('0b','')[::-1]
                            for m in range(lls_str.__len__()):
                                if lls_str[m]=='1':
                                    # print(type(str(m)))
                                    # print(type(lls))
                                    str_lls=lls_dic[m]
                            print(lls_str)
                if i==2:
                    series=row[i]

            temp_list = [mac, off_on, system_model, szwd, str_lls, series]
            a.append(temp_list)
    test = pd.DataFrame(columns=title, data=a)
    test.to_csv('e:/testcsv_1.csv', encoding='gb18030')



if __name__=='__main__':
    print('starttime:'+str(datetime.now()))
    read_csv()
    print('donetime:'+str(datetime.now()))

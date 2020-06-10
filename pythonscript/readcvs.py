# -*- coding: utf-8 -*-
# @Time    : 2020-6-10 10:39 
# @Author  : 081191 
# @FileName: readcvs.py                     
# @Software: PyCharm 
# !/usr/bin/python


import pandas as pd
import xlrd
import re
from datetime import datetime

print('starttime:' + str(datetime.now()))
a=[]
title = [U'热水器名称', U'系列', U'品类', U'状态', U'MAC地址', U'用水累加量',U'用气累加量',U'零冷水模式',U'水增压+:',U'点动+:',U'单巡航:',U'零冷水预约状态模式',U'在线状态']  # 表格title
def read_csv():
    data=xlrd.open_workbook('siv_3.xls')  #Excel文档存储路径：C:\Python27
    table=data.sheets()[0]  #按索引获取sheet
    nrows=table.nrows  #行数

    for rownum in range(1,nrows):
        row=table.row_values(rownum)   #循环读取每一行的value，存入变量row
        if row:
            modelname=row[1]
            seriesname=row[2]
            category=row[3]
            status=row[4]
            mac=row[5]
            statusInfo=row[6]
            matchobj0 = re.search(r'用水[\u4e00-\u9fa5]+.*', statusInfo)
            if matchobj0:
                ys = re.search(r'\d+', matchobj0.group()).group(0)
            matchobj1 = re.search(r'用气[\u4e00-\u9fa5]+.*', statusInfo)
            if matchobj1:
                yq = re.search(r'\d+', matchobj1.group()).group(0)
            matchobj2 = re.search(r'零冷水模[\u4e00-\u9fa5]+.*', statusInfo)
            if matchobj2:
                llsinfo = re.search(r'\([\u4e00-\u9fa5]+.*', matchobj2.group()).group().replace('(', '').replace(')','').split(' ')
                print(llsinfo)
                llszt = llsinfo[0].replace('零冷水状态:', '')
                szy = llsinfo[1].replace('水增压+:', '')
                dd = llsinfo[2].replace('点动:', '')
                dxh = llsinfo[3].replace('单巡航:', '')
            matchobj3 = re.search(r'零冷水预约[\u4e00-\u9fa5]+.*', statusInfo)
            if matchobj3:
                yyms = matchobj3.group().replace('零冷水预约状态模式:', '')
            else:
                yyms=''
            online=row[7]
            temp_list = [modelname,seriesname,category,status,mac,ys,yq,llszt,szy,dd,dxh,yyms,online]
            a.append(temp_list)
            print(temp_list, file=open('../test1.txt', 'a+', encoding='UTF-8'))
        print(a.__len__())
    test = pd.DataFrame(columns=title, data=a)
    test.to_csv('e:/testcsv.csv', encoding='gb18030')




if __name__=='__main__':

    read_csv()
    print('donetime:'+str(datetime.now()))
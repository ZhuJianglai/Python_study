# -*- coding: utf-8 -*-
# @Time    : 2020-6-9 15:20
# @Author  : 081191 
# @FileName: ReadJson.py                     
# @Software: PyCharm 
# !/usr/bin/python


import json
import re
import pandas as pd
from datetime import datetime
import time
a=[]
title = [U'时间',U'brand', U'category', U'deviceId', U'model', u'series', U'用水累加量',U'用气累加量',U'零冷水模式',U'水增压+',U'点动+',U'单巡航',U'零冷水预约状态模式']  # 表格title
def readjson():
    with open('data_20200609_012444.txt', 'r', encoding='utf-8') as f1:

        for line in f1.readlines():
            line1=json.loads(line)
            if line1['category']=='燃气热水器':
                localtime=time.localtime(int(line1['__time__']))
                timestr=time.strftime('%Y:%m:%d %H:%M:%S',localtime)
                brand = line1['brand']
                category = line1['category']
                deviceId = line1['deviceId']
                model = line1['model']
                series = line1['series']
                for i in range(len(line1['statusInfo'].split('\n'))):
                    strinfo = line1['statusInfo'].split('\n')[i]
                    # print('-' * i + strinfo)
                    matchobj0=re.search(r'用水[\u4e00-\u9fa5]+.*',strinfo)
                    if matchobj0:
                        ys=re.search(r'\d+',matchobj0.group()).group(0)
                    matchobj1=re.search(r'用气[\u4e00-\u9fa5]+.*',strinfo)
                    if matchobj1:
                        yq=re.search(r'\d+',matchobj1.group()).group(0)
                    matchobj2 = re.search(r'零冷水模[\u4e00-\u9fa5]+.*', strinfo)
                    if matchobj2:
                        llsinfo=re.search(r'\([\u4e00-\u9fa5]+.*',matchobj2.group()).group().replace('(','').replace(')','').split(' ')
                        print(llsinfo)
                        llszt=llsinfo[0].replace('零冷水状态:','')
                        szy=llsinfo[1].replace('水增压+:','')
                        dd=llsinfo[2].replace('点动:','')
                        dxh=llsinfo[3].replace('单巡航:','')
                    matchobj3 = re.search(r'零冷水预约[\u4e00-\u9fa5]+.*', strinfo)
                    if matchobj3:
                        yyms=matchobj3.group().replace('零冷水预约状态模式:','')
                    else:
                        yyms=''
            temp_list = [timestr,brand,category,deviceId,model,series,ys,yq,llszt,szy,dd,dxh,yyms]
            a.append(temp_list)
            print(temp_list, file=open('../test1.txt', 'a+', encoding='UTF-8'))
        print(a.__len__())
    test = pd.DataFrame(columns=title, data=a)
    test.to_csv('e:/testcsv_1.csv', encoding='gb18030')




if __name__=='__main__':
    print('starttime:'+str(datetime.now()))
    readjson()
    print('donetime:'+str(datetime.now()))
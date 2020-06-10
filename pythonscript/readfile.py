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


a=[]
title = [U'brand', U'category', U'deviceId', U'model', u'series',U'用水累加量',U'用气累加量',U'零冷水状态',U'水增压',U'点动',U'单循行',u'零冷水预约状态模式']  # 表格title
def readjson():
    with open('data_20200609_012444.txt', 'r', encoding='utf-8') as f1:
        # list1=f1.readlines()[1]
        # list1=json.loads(list1)
        # print(type(list1))
        # print(list1['brand'])

        for line in f1.readlines():
            line1=json.loads(line)

            if line1['category']=='燃气热水器':
                # print(line1,file=open('test','a+',encoding='UTF-8'))
                # print(type(line1['statusInfo']))
                # statusInfo='{"'+line1['statusInfo'].replace('\n','","').replace(':','":"')+'}'
                brand = line1['brand']
                category = line1['category']
                deviceId = line1['deviceId']
                model = line1['model']
                series = line1['series']
                str1=''
                for i in range(len(line1['statusInfo'].split('\n'))):

                    strinfo = line1['statusInfo'].split('\n')[i]
                    # print('-' * i + strinfo)
                    matchobj1=re.match(r'设备[\u4e00-\u9fa5]+.*',strinfo)
                    matchobj2 = re.match(r'零冷水模[\u4e00-\u9fa5]+.*', strinfo)
                    matchobj3 = re.match(r'滤芯[\u4e00-\u9fa5]+.*', strinfo)
                    if matchobj1 or matchobj2 or matchobj3:
                        strinfo1='"'+strinfo.replace(':(','":"(')+'"'
                        # print('-' * i + strinfo)
                    else:
                        strinfo1='"'+strinfo.replace(':','":"')+'"'
                    str1=str1+strinfo1+','
                json_list='{'+str1.replace(',"",','')+'}'
                # print(json_list)
                new_line=json.loads(json_list)
                # print(new_line['系统模式'])
                ys = new_line['用水累加量']
                yq = new_line['用气累加量']
                llsms = new_line['零冷水模式'].replace('零冷水模式:(','').replace(')','').split(' ')
                llszt = llsms[0].replace('(零冷水状态:', '')
                szy = llsms[1].replace('水增压+:', '')
                dd = llsms[2].replace('点动:', '')
                dxh = llsms[3].replace('单巡航:', '')
                # print(llsms)
                if '零冷水预约状态模式' in new_line:
                    llsyyztms = new_line['零冷水预约状态模式']
                else:
                    llsyyztms=''
                # if '滤芯设置状态' in new_line:
                #     lxsz = new_line['滤芯设置状态']
                # else:
                #     lxsz=''
            temp_list = [brand,category,deviceId,model,series,ys,yq,llszt,szy,dd,dxh,llsyyztms]
            a.append(temp_list)
            # print(temp_list, file=open('test1.txt', 'a+', encoding='UTF-8'))
        print(a.__len__())
    test = pd.DataFrame(columns=title, data=a)
    test.to_csv('e:/testcsv_0.csv', encoding='gb18030')




if __name__=='__main__':
    print('starttime:'+str(datetime.now()))
    readjson()
    print('donetime:'+str(datetime.now()))
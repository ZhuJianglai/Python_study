# -*- coding: utf-8 -*-
# @Time    : 2020-6-9 15:20 
# @Author  : 081191 
# @FileName: ReadJson.py                     
# @Software: PyCharm 
# !/usr/bin/python


import json
import re
import pandas as pd

title = [U'brand', U'category', U'deviceId', U'model', u'series',U'statusInfo',U'用水累加量',U'用气累加量',U'零冷水模式',U'零冷水预约状态模式',U'滤芯设置状态']  # 表格title
def readjson():
    with open('data_20200609_012444.txt', 'r', encoding='UTF-8') as f1:
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
                statusInfo = line1['statusInfo']
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
                llsms = new_line['零冷水模式']
                if '零冷水预约状态模式' in new_line:
                    llsyyztms = new_line['零冷水预约状态模式']
                else:
                    llsyyztms=''
                if '滤芯设置状态' in new_line:
                    lxsz = new_line['滤芯设置状态']
                else:
                    lxsz=''
            temp_list = [brand,category,deviceId,model,series,statusInfo,ys,yq,llsms,llsyyztms,lxsz]
            print(temp_list, file=open('../test1.txt', 'a+', encoding='UTF-8'))
    # test = pd.DataFrame(columns=title, data=temp_list)
    # # test.to_csv('e:/testcsv.csv', encoding='gbk')
    # test.to_csv(test+'.csv', encoding='gbk')




if __name__=='__main__':
    readjson()
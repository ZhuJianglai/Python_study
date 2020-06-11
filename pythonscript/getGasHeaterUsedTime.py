# -*- coding: utf-8 -*-
# @Time    : 2020-6-10 16:18 
# @Author  : 081191 
# @FileName: getGasHeaterUsedTime.py                     
# @Software: PyCharm 
# !/usr/bin/python

import requests
import json

# import geventwebsocket

_API_URL = 'https://rubyapi.vanward.com'
_HEADERS = {"Content-Type" : "application/x-www-form-urlencoded"}

 #获取用户用水时间
def getGasHeaterUsedTime():
    key='9cf9b09c24d8490c86b3c9a16bb6d3a0'
    r = requests.post(_API_URL + '/api/autotest/getGasHeaterUsedTime', params = {'deviceId':key,'sign':'312sda7xhj290derw343213sdw'}, headers = _HEADERS)
    usedtime = json.loads(r.content.decode())
    try:

        temp_date=list(usedtime)
        for i in range(len(temp_date)):
            addDate=temp_date[i]['addDate']
            timeFrameIndex=temp_date[i]['timeFrameIndex']

            print(addDate,timeFrameIndex)


    except json.decoder.JSONDecodeError as e:
        print(e.msg)




if __name__ == '__main__':
    getGasHeaterUsedTime()

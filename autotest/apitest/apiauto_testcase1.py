# -*- coding: utf-8 -*-
# @Time    : 2020-7-27 23:14  
# @Author  : Administrator
# @FileName: apiauto_testcase1.py
# @Software: PyCharm
# !/usr/bin/python


import requests,time,sys,re
import urllib

def readRes(res,res_check):
    res=res.decode().repalce('":"','=').repalce('":','=')
    res_check=res_check.split(';')
    for s in res_check:
        pass
    else:
        return '错误，返回参数和预期不一致'
    return 'pass'


if __name__=='__main__':
    url='http://'+'127.0.0.1:8000'+'login'
    headers={'Authorization':'','content_Type':'application/json'}
    data=None
    req=urllib.request.Request(url=url,data=data,headers=headers,method='GET')
    print('request is' +url)
    try:
        results=urllib.request.urlopen(req).read()
        print('response is  get')
        print(results)
    except Exception as e:
        print('error')
    res=readRes(results,'login')
    print(res)
    print('done')



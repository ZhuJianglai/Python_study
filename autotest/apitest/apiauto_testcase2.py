# -*- coding: utf-8 -*-
# @Time    : 2020-7-28 0028 19:23 
# @Author  : 081191 
# @FileName: apiauto_testcase2.py                     
# @Software: PyCharm 
# !/usr/bin/python

import pymysql
import re
import json
import requests
import time
def test_readSQLcase():
    sql="select id,apiname,apiurl,apimethod,apiparamvalue,apiresult,apistatus from autotest.apitest_apis"
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port='3306',host='127.0.0.1',charser='utf8')
    cursor=coo.cursor()
    aa=cursor.execute(sql)
    info=cursor.fetchmany(aa)
    for ii in info:
        case_list=[]
        case_list.append(ii)
        interfaceTest(case_list)
    coo.commit()
    cursor.close()
    coo.close()

def interfaceTest(case_list):
    res_flags=[]
    request_url=[]
    response=[]
    strinfo=re.compile('{seturl}')
    for case in case_list:
        try:
            case_id=case[0]
            interface_name=case[1]
            method=case[3]
            url=case[2]
            param=case[4]
            res_check=case[5]
        except Exception as e:
            return '测试用例格式不正确！%s'%e
        if param=='':
            new_url='http://'+'api.test.com.cn'+url
        elif param=='null':
            url=strinfo.sub(str(seturl('seturl')),url)
            new_url='http://'+url
        else:
            url = strinfo.sub(str(seturl('seturl')), url)
            new_url='http://'+'127.0.0.1'+url
            request_url.append(new_url)
        if method.upper()=='GET':
            headers={'Authorizations':'','Content-Type':'application/json'}
            if "=" in ur




def readRes(res,res_check):
    res=res.decode().replace('":"',"=").replace('":','=')
    res_check=res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return '错误返回参数与预期不一致'
    return 'pass'

def urlParam(param):
    param1=param.replace('&quot;','"')
    return param1

def CredentialId():
    global id
    url='http://'+'api.com.cn'+'/api/Security/Authentication/Signin/web'
    body_data=json.dumps({'Identity':'admin',"Passwrd":'1234567a'})
    headers={'Connection':'keep-alive','Content-Type':'application/json'}
    response=requests.post(url=url,data=body_data,headers=headers)
    data=response.text
    regx='.*"CredentialId":"(.*)","Scene"'
    pm=re.search(regx,data)
    id=pm.group(1)

def seturl(set):
    global seturl()
    sql="select setname,setvalue from set_set"
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor=coo.cursor()
    aa=cursor.execute(sql)
    info=cursor.fetchmany(aa)
    print(info)
    coo.commit()
    cursor.close()
    if info[0][0]==set:
        setvalue=info[0][1]
        print(setvalue)
    return setvalue

def writeResult(case_id,result):
    result=result.encode('utf-8')
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    sql='update apitest_apistep set apitest_apitest.apisstatus=%s,apitest_apistep.create_time=%s where apitest_apistep.id=%s;'
    param=(result,now,case_id)
    print('api autotest resule is '+result.decode())
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor=coo.cursor()
    cursor.execute(sql,param)
    coo.commit()
    cursor.close()
    coo.close()


def caseWriteResult(case_id,result):
    result=result.encode('utf-8')
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    sql='update apitest_apis set apitest_apis.apistatus=%s,apitest_apis.create_time=%s where apitest_apis.id=%s;'
    param=(result,now,case_id)
    print('api autotest resule is '+result.decode())
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor=coo.cursor()
    cursor.execute(sql,param)
    coo.commit()
    cursor.close()
    coo.close()

def writeBug(bug_id,interface_name,request,response,res_check):
    interface_name=interface_name.encode('utf-8')
    res_check=res_check.encode('utf_8')
    request=request.encode('utf-8')





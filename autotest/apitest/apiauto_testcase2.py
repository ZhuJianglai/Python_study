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
import urllib
def test_readSQLcase():
    sql="select id,apiname,apiurl,apimethod,apiparamvalue,apiresult,apistatus from autotest.apitest_apis"
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
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
        print(method.upper())
        if method.upper()=='1':
        # if method.upper() == 'GET':
            headers={'Authorizations':'','Content-Type':'application/json'}
            if "=" in urlParam(param):
                data=None
                print(str(case_id)+'request is get'+new_url.encode('utf-8')+'?'+urlParam(param).encode('utf-8'))
                result=requests.get(new_url+'?'+urlParam(param),data,headers=headers).text
                print('response is get'+result.encode('utf-8'))
                response.append(result)
                res=readRes(result,'')
            else:
                print('request is get'+new_url+'body is '+urlParam(param))
                data=None
                req=urllib.request.Request(url=new_url,data=data,headers=headers,method='GET')
                try:
                    result=urllib.request.urlopen(req).read()
                    print('response is get')
                    print(result)
                except Exception as e:
                    return caseWriteResult(case_id,0)
                res=readRes(result,res_check)
                if 'pass' == res:
                    res_flags.append('pass')
                    writeResult(case_id,'1')
                    caseWriteResult(case_id,'1')
                else:
                    res_flags.append('fail')
                    writeResult(case_id,'0')
                    caseWriteResult(case_id,'0')






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
    global setvalue
    sql="select setname,setvalue from set_set"
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor=coo.cursor()
    aa=cursor.execute(sql)
    info=cursor.fetchmany(aa)
    print(info)
    coo.commit()
    cursor.close()
    for ii in info:
    # if info[0][0]==set:
    #     setvalue=info[0][1]
    #     print(setvalue)
        if ii[0]==set:
            setvalue=ii[1]
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
    now=time.strftime('%Y-%m-%d %H:%M:%S')
    bug_name=str(bug_id)+'_'+interface_name.decode()+'_出错了'
    bugdetail='[请求数据]<br />'+request.decode()+'<br/>'+'[预期结果]<br />'+res_check.decode()+'<br />'+'<br />'+'[响应数据]<br />'+'<br />'+response.decode()
    print(bugdetail)
    sql="insert into bug_bug ('bug_name','bugdetail','bugstatus','buglevel','bugcreater','bugassign',create_time','Product_id')values(%s,%s,'1','1','邹辉','邹辉',%s,'2)"%(bug_name,pymysql.escape_string(bugdetail),now)
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor=coo.cursor()
    cursor.execute(sql)
    coo.commit()
    cursor.close()
    coo.close()



if __name__=='__main__':
    test_readSQLcase()
    print('Done')
    time.sleep(1)





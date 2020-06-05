# -*- coding: utf-8 -*-
import requests,time,sys,re
import urllib,zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep

import HTMLTestRunner
import unittest




HOSTNAME='127.0.0.1'





def readSQLcase():
    sql='SELECT id,apiname,apiurl,apimethod,apiparamvalue,apiresult,apistatus FROM apitest_apistep WHERE apitest_apistep.Apitest_id =3'
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',charset='utf8')
    cursor=coo.cursor()
    aa=cursor.execute(sql)
    info=cursor.fetchmany(aa)
    for ii in info:
        case_list=[]
        case_list.append()
        # CredentialId()
        interfaceTest(case_list)
    coo.commit()
    cursor.close()
    coo.close()

def interfaceTest(case_list):
    res_flags=[]
    request_urls=[]
    responses=[]
    strinfo=re.compile('{TaskId}')
    strinfo1=re.compile('{AaaetId}')
    strinfo2=re.compile('{PointId}')
    assetinfo=re.compile('{assetno}')
    tasknoinfo=re.compile('{taskno}')
    schemainfo=re.compile('{schema}')
    for case in case_list:
        try:
            case_id= case[0]
            interface_name=case[1]
            method=case[3]
            url=case[2]
            param=case[4]
            res_check=case[5]
        except Exception as e:
            return '测试用例格式不正确%s'%e

        if param=='':
            new_url='http://'+'api.test.com.cn'+url
        elif param=='null':
            new_url='http://'+url
        else:
            url=strinfo.sub(TaskId,url)
            param=strinfo.sub(TaskId,param)
            param=tasknoinfo.sub(taskno,param)
            new_url='http://127.0.0.1'+url
        if method.upper()=='GET':
            headers ={'Authorization':'','Content-type':'appliacation/json'}
            if "=" in urlParam(param):
                date=None
                print(str(case_id)+'request is get'+new_url.encode('utf-8')+'?'+urlParam(param).encode('utf-8'))
                results=requests.get(new_url+'?'+urlParam(param),date,headers=headers).text
                print('response is get'+results.encode('utf-8'))
                responses.append(results)
                res=readRes(results,'')
            else:
                print('request is get'+new_url+'body is' +urlParam(param))
                date=None
                req=urllib.request.Request(url=new_url,date=date,headers=headers,method='GET')
                results=urllib.request.urlopen(req).read()
                print('response is get')
                print(results)
                res=readRes(results,res_check)
            if 'pass'==res:
                writeResult(case_id,'1')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id,'0')
            if method.upper() =='PUT':
                headers ={'Host':HOSTNAME,'Connection':'keep-alive','CredentialId':id,'Content-type':'appliacation/json'}
                body_data=param
                results=requests.put(url=url,date=body_data,headers=headers)
                responses.append(results)
                res=readRes(results,res_check)
                if 'pass'==res:
                    writeResult(case_id,'pass')
                    res_flags.append('pass')
                else:
                    writeResult(case_id,'fail')
                    res_flags.append('fail')
                    writeBug(case_id,interface_name,new_url,results,res_check)
                try:
                    preOrderSN(results)
                except:
                    print('ok')
            if method.upper()=='PATCH':
                headers ={'Authorization':'CredentialId'+id,'Content-type':'appliacation/json'}
                data=None
                results=requests.patch(new_url+'?'+urlParam(param),date,headers=headers).text
                responses.append(results)
                res=readRes(results,res_check)
                if 'pass'==res:
                    writeResult(case_id,'pass')
                    res_flags.append('pass')
                else:
                    res_flags.append('fail')
                    writeResult(case_id,'fail')
                    writeBug(case_id,interface_name,new_url,results,res_check)

                try:
                    preOrderSN(results)
                except:
                    print('ok')
            if method.upper=='POSt':
                headers ={'Authorization':'CredentialId'+id,'Content-type':'appliacation/json'}
                if "=" in urlParam(param):
                    date=None
                    results=requests.patch(new_url+'?'+urlParam(param),date,headers=headers).text
                    print('response is post'+results.encode('utf-8'))
                    responses.append(results)
                    res=readRes(results,'')
                else:
                    print(str(case_id)+'request is'+new_url.encode('utf-8')+'body is'+urlParam(param).encode('utf-8'))
                    results=requests.post(new_url,date=urlParam(param).encode('utf-8'),headers=headers).text
                    print('response is post'+results.encode('utf-8'))
                    responses.append(results)
                    res=readRes(results,res_check)
                    if 'pass'==res:
                        writeResult(case_id,'1')
                        res_flags.append('pass')
                    else:
                        res_flags.append('fail')
                        writeResult(case_id,'0')
                        writeBug(case_id,interface_name,new_url,results,res_check)
                    try:
                        TaskId(results)
                    except:
                        print('ok1')



def readRes(res,res_check):
                    res=res.decode().replace('":"',"=").replace('":"',"=")
                    res_check=res_check.split(',')
                    for s in res_check:
                        if s in res:
                            pass
                        else:
                            return '错误，返回参数和预期不一样'

                    return 'pass'

def urlParam(param):
    param1=param.replace('&quot;','"')
    return param1


def creadentiaId():
    global id
    url="http://"+'api.test.com.cn'+'/api/Security/Authentication/Signin/web'
    body_data=json.dumps({'Identity':'test','Password':'test'})
    headers={'Connection':'keep-alive','Content-Type':'application/json'}
    response=requests.post(url=url,data=body_data,headers=headers)
    data=response.text
    regx='.*"CredentialId":"(.*)","Scene"'
    pm=re.search(regx,data)
    id=pm.group()


def preOrderSN(results):
    global preOrderSN
    regx='.*"preOrderSN":"（.*)","toHome"'
    pm=re.search(regx,results)
    if pm:
        preOrderSN =pm.group(1).encode('utf-8')
        return preOrderSN
    return False


def TaskId(results):
    global TaskId
    regx='.*"TaskId"(.*),"PlanId"'
    pm=re.search(regx,results)
    if pm:
        TaskId =pm.group(1).encode('utf-8')
        return TaskId
    return False


def taskno(param):
    global taskno
    a=int(time.time())
    taskno='task_'+str(a)
    return taskno



def writeResult(case_id,result):
    result=result.encode('utf-8')
    now =time.strftime("%Y-%m-%d %H:%M:%S")
    sql="UPDATE apitest_apistep SET apitest_apistep.apistatus=%s WHERE apitest_apistep.Apitest_id=%s"
    parma=(result,case_id)
    print('api autotest result is '+result.decode())
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',chartset='utf-8')
    cursor=coo.cursor()
    cursor.execute(sql,parma)
    coo.commit()
    cursor.close()
    coo.close()



def writeBug(bug_id,interface_name,request,response,res_check):
    interface_name=interface_name.encode('utf-8')
    res_check=res_check.encode('utf-8')
    request=request.encode('utf-8')
    now=time.strftime("%Y-%m-%d %H:%M:%S")
    bug_name=str(bug_id)+"_"+interface_name.decode()+'_出错了'
    bugdetail='[请求数据]<br />'+request.decode()+'<br />'+'<br />'+'[预期结果]<br />'+res_check.decode()+'<br />'+'<br />'+'[响应数据]<br />'+response.decode()
    print(bugdetail)
    sql='INSERT INTO bug_bug(bugname,bugdetail,bugstatus,buglevel,bugcreater,bugassign create_time,Product_id) VALUES(%s,%s,1,1,'+'zhuning','zhuning'+',%s,2);'%(bug_name,pymysql.escape_string(bugdetail),now)
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',chartset='utf-8')
    cursor=coo.cursor()
    cursor.execute(sql)
    coo.commit()
    cursor.close()
    coo.close()


if __name__=='__main__':
    readSQLcase()
    print('Done')
    time.sleep(1)



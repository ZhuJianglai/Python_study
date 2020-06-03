# -*- coding: utf-8 -*-
import requests,time,sys,re
import urllib,zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep


HOST='127.0.0.1'

def readSQLcase():
    sql='SELECT id,apiname,apiurl,apimethod,apiparamvalue,apiresult,apistatus FROM apitest_apistep WHERE apitest_apistep.Apitest_id =3'
    coo=pymysql.connect(user='root',passwd='1234567a',db='autotest',port=3306,host='127.0.0.1',chartset='utf8')
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
                results=requests.get(new_url+'?'+urlrlParm(param),date,headers=headers).text
                print('response is get'+results.encode('utf-8'))
                responses.append(results)
                res=readRes(results,'')
            else:
                print('request is get'+new_url+'body is' +ur





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






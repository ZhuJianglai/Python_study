import pymysql
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Apitest,Apistep,Apis
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger





doc = open("test.log", "a+")
# Create your views here.
def test(request):
    return HttpResponse("hello test")


def login(request):
    # doc = open("test.log", "a+")
    if request.POST:
        username = password = ''
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        bool= False
        print(username, password, file=doc)
        if user is not None and user.is_active :
            auth.login(request,user)
            request.session['user']=username
      # if username=='123' and password== '123':
            bool=True
            print(bool,file=doc)
            response =HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'username or password error'})
    return render(request,'login.html')


def home(request):
    return render(request,"home.html")


def logout(request):
    auth.logout(request)
    return render(request,'login.html')

#接口管理
@login_required
def apitest_manage(request):

    apitest_list =Apitest.objects.all()  #读取所有流程接口数据
    apitest_count=Apitest.objects.all().count() #统计数量
    username=request.session.get('user','') #读取浏览器登录session
    # 20200630添加翻页功能
    paginator=Paginator(apitest_list,8) #生成paginator对象，设置每页显示8条记录
    page=request.GET.get('page',1)#获取当前页码数，默认为第一页
    currentPage=int(page)
    try:
        apitest_list=paginator.page(page)#获取当前页码数的记录
    except PageNotAnInteger:
        apitest_list=paginator.page(1)#如果输入的页码不是整数，则显示第一页内容
    except EmptyPage:
        apitest_list=paginator.page(paginator.num_pages)#如果输入的页数不在系统中，则显示最后一页

    return render(request,'apitest_manage.html',{"user":username,"apitests":apitest_list,"apitestcount":apitest_count})#定义流程接口数据的变量并返回到前端
#
# 接口步骤管理（20200717修改）
# @login_required
# def apistep_manage(request):
#     username=request.session.get('user','')
#     apistep_list=Apistep.objects.all()
#     apistep_count=Apistep.objects.all().count()
#     paginator=Paginator(apistep_list,8)
#     page=request.GET.get('page',1)
#     currentPage=int(page)
#     try:
#         apistep_list=paginator.page(page)
#     except PageNotAnInteger:
#         apistep_list=paginator.page(1)
#     except EmptyPage:
#         apistep_list=paginator.page(paginator.num_pages)
#     return render(request,'apistep_manage.html',{'user':username,'apisteps':apistep_list,"apistepcount":apistep_count})
@login_required
def apistep_manage(request):
    username=request.session.get('user','')
    apitestid=request.GET.get('apitest.id',None)
    apitest=Apitest.objects.get(id=apitestid)
    print(apitestid)
    print(apitest)
    apistep_list=Apitest.objects.all()
    return render(request,'apistep_manage.html', {'user': username, 'apitest': apitest,'apisteps':apistep_list})



#单一接口测试用例
@login_required
def apis_manage(request):
    username=request.session.get('user','')
    apis_list=Apis.objects.all()
    apis_count = Apis.objects.all().count()
    paginator=Paginator(apis_list,8)
    page=request.GET.get('page',1)
    currentPage=int(page)
    try:
        apis_list=paginator.page(page)
    except PageNotAnInteger:
        apis_list=paginator.page(1)
    except EmptyPage:
        apis_list=paginator.page(paginator.num_pages)
    return render(request,'apis_manage.html',{'user':username,'apiss':apis_list,"apiscount":apis_count})


#测试报告
@login_required
def test_report(request):
    username=request.session.get('user','')
    apis_list = Apis.objects.all()
    apis_count=Apis.objects.all().count()#统计接口数
    db=pymysql.connect(user='root',db='autotest',passwd='1234567a',host='127.0.0.1')
    cursor=db.cursor()
    sql1='select count(id) from apitest_apis where apitest_apis.apistatus=1'
    aa =cursor.execute(sql1)
    apis_pass_count=[row[0] for row in cursor.fetchmany(aa)][0]
    sql2='select count(id) from apitest_apis where apitest_apis.apistatus=0'
    bb=cursor.execute(sql2)
    apis_fail_count=[row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request,'report.html',{'user':username,'apiss':apis_list,'apiscounts':apis_count,'apis_pass_count':apis_pass_count,'apis_fail_count':apis_fail_count})



def left(request):
    return render(request,"left.html")



#搜索功能
@login_required
def apisearch(request):
    username=request.session.get('user','')
    search_apitestname=request.GET.get("apitestname",'')
    apitest_list=Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request,'apitest_manage.html',{"user":username,"apitests":apitest_list})


@login_required
def apissearch(request):
    username=request.session.get('user','')
    search_apiname=request.GET.get('apiname','')
    apis_list=Apis.objects.filter(apisname__icontains=search_apiname)
    return render(request,'apis_manage.html',{"user":username,'apiss':apis_list})


@login_required
def apistepsearch(request):
    username=request.session.get('user','')
    search_apistepname=request.GET.get('apistepname','')
    apistep_list=Apis.objects.filter(apistepname__icontains=search_apistepname)
    return render(request,'apistep_manage.html',{"user":username,'apiss':apistep_list})



def welcome(request):
    return  render(request,"welcome.html")
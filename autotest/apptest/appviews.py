from django.contrib.auth.decorators import login_required
from apptest.models import Appcase,Appcasestep

from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
# app用例管理
@login_required
def appcase_manage(request):
    appcase_list=Appcase.objects.all()
    appcase_count=Appcase.objects.all().count()
    username=request.session.get('user','')
    paginator=Paginator(appcase_list,8)
    page=request.GET.get('page',1)
    currentPage=int(page)
    try:
        appcase_list=paginator.page(page)
    except PageNotAnInteger:
        appcase_list=paginator.page(1)
    except EmptyPage:
        appcase_list=paginator.page(paginator.num_pages)
    print(username)
    return render(request,'appcase_manage.html',{'user':username,'appcases':appcase_list,"appcasecount":appcase_count})


# # APP用例测试步骤
# @login_required
# def appcasestep_manage(request):
#     username =request.session.get('user','')
#     # appcasestep_list=Appcasestep.objects.all()
#     appcaseid=request.GET.get('appcase.id',None)
#     appcase=Appcase.objects.get(id=appcaseid)
#     print(appcase)
#     appcasestep_list = Appcasestep.objects.all()
#     print(appcasestep_list)
#     appcasestep_count=Appcasestep.objects.all().count()
#     paginator=Paginator(appcasestep_list,8)
#     page=request.GET.get('page',1)
#     currentPage=int(page)
#     try:
#         appcase_list=paginator.page(page)
#     except PageNotAnInteger:
#         appcase_list=paginator.page(1)
#     except EmptyPage:
#         appcase_list=paginator.page(paginator.num_pages)
#     return render(request,'appcasestep_manage.html',{'user':username,'appcase':appcase,'appcasesteps':appcasestep_list,"appcasestepcount":appcasestep_count})
# APP用例测试步骤
@login_required
def appcasestep_manage(request):
    username =request.session.get('user','')
    appcaseid=request.GET.get('appcase.id',None)
    print('appcaseid:'+str(appcaseid))
    appcase=Appcase.objects.get(id=appcaseid)
    print(appcase)
    appcasestep_list = Appcasestep.objects.all()
    print(appcasestep_list)
    return render(request,'appcasestep_manage.html',{'user':username,'appcase':appcase,'appcasesteps':appcasestep_list})





@login_required
def appsearch(request):
    username=request.session.get('user','')
    search_appcasename=request.GET.get("appcasename",'')
    appcase_list=Appcase.objects.filter(appcasename__icontains=search_appcasename)
    return render(request,'appcase_manage.html',{'user':username,"bugs":appcase_list})



@login_required
def appstepsearch(request):
    username=request.session.get('user','')
    search_appcasestepname=request.GET.get("appcasestepname",'')
    appcasestep_list=Appcase.objects.filter(appcasestepname__icontains=search_appcasestepname)
    return render(request,'appcase_manage.html',{'user':username,"bugs":appcasestep_list})
from django.contrib.auth.decorators import login_required
from apptest.models import Appcase,Appcasestep

from django.shortcuts import render



# Create your views here.
# app用例管理
@login_required
def appcase_manage(request):
    appcase_list=Appcase.objects.all()
    username=request.session.get('user','')
    print(username)
    return render(request,'appcase_manage.html',{'user':username,'appcases':appcase_list})


# APP用例测试步骤
@login_required
def appcasestep_manage(request):
    username =request.session.get('user','')
    appcasestep_list=Appcasestep.objects.all()
    return render(request,'appcasestep_manage.html',{'user':username,'appcasestep':appcasestep_list})


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
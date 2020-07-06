from django.contrib.auth.decorators import login_required
from webtest.models import Webcase,Webcasestep

from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
# web用例管理
@login_required
def webcase_manage(request):
    webcase_list=Webcase.objects.all()
    username=request.session.get('user','')
    webcase_count=Webcase.objects.all().count()
    paginator=Paginator(webcase_list,8)
    page=request.GET.get('page',1)
    crrentPage=int(page)
    try:
        webcase_list=paginator.page(page)
    except PageNotAnInteger:
        webcase_list=paginator.page(1)
    except EmptyPage:
        webcase_list=paginator.page(paginator.num_pages)
    print(username)
    return render(request,'webcase_manage.html',{'user':username,'webcases':webcase_list,'webcasecount':webcase_count})


# web用例测试步骤
@login_required
def webcasestep_manage(request):
    username =request.session.get('user','')
    print(username)
    webcasestep_list=Webcasestep.objects.all()
    webcasestep_count=Webcasestep.objects.all().count()
    paginator=Paginator(webcasestep_list,8)
    page=request.GET.get('page',1)
    crrentPage=int(page)
    try:
        webcasestep_list=paginator.page(page)
    except PageNotAnInteger:
        webcasestep_list=paginator.page(1)
    except EmptyPage:
        webcasestep_list=paginator.page(paginator.num_pages)
    return render(request,'webcasestep_manage.html',{'user':username,'webcasesteps':webcasestep_list,'webcasestepcount':webcasestep_count})

# web搜索功能
@login_required
def websearch(request):
    username=request.session.get('user','')
    search_webcasename=request.GET.get('webcasename','')
    print("search_webcasename:"+search_webcasename)
    webcase_list=Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request,'webcase_manage.html',{'user':username,"webcases":webcase_list})

#webcasesetp搜索功能
@login_required
def webstepsearch(request):
    username=request.session.get('user','')
    search_webcasestepname=request.GET.get('webcasestepname','')
    webcasestep_list=Webcasestep.objects.filter(webteststep__icontains=search_webcasestepname)
    return render(request,'webcasestep_manage.html',{'user':username,"webcasesteps":webcasestep_list})


from django.shortcuts import render
from bug.models import Bug
from django.contrib.auth.decorators import login_required
# Create your views here.
#bug管理
def bug_manage(request):
    username =request.session.get('user','')
    bug_list=Bug.objects.all()
    return render(request,'bug_manage.html',{'user':username,'bugs':bug_list})




@login_required
def bugsearch(request):
    username=request.session.get('user','')
    print(username)
    search_bugname=request.GET.get("bugname",'')
    print(search_bugname)
    bug_list=Bug.objects.filter(bugname__icontains=search_bugname)
    return render(request,'bug_manage.html',{'user':username,"bugs":bug_list})

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login

# Create your views here.
def test(request):
    return HttpResponse("hello test")


def login(request):
    if request.POST:
        username = password = ''
        username=request.POST.get('username')
        password=request.POST.get('password')
        # user=auth.authenticate(username=username,password=password)
        # if user is not None and user.is_active :
        #     auth.login(request,user)
        #     request.session['user']=username
        print(username,password)
        if username==123 and password==123:
            response =HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'username or password error'})

    return render(request,'login.html')


def home(request):
    return render(request,"home.html")

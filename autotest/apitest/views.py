from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login

# Create your views here.
def test(request):
    return HttpResponse("hello test")


def login(request):
    doc = open("test.log", "a+")
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
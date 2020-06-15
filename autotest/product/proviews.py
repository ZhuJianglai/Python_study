from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

#产品管理
def product_manage(request):
    doc = open("test.log", "a+")
    username=request.session.get('user','')
    product_list=Product.objects.all()
    print(product_list,file=doc)
    return render(request,'product_manage.html',{"user":username,'products':product_list})



#搜索功能
@login_required
def productsearch(request):
    username=request.session.get('user','')
    search_productname=request.GET.get("apitestname",'')
    product_list=Product.objects.filter(productname__icontains=search_productname)
    return render(request,'product_manage.html',{"user":username,"apitests":product_list})
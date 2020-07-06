from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

#产品管理
def product_manage(request):
    doc = open("test.log", "a+")
    username=request.session.get('user','')
    product_list=Product.objects.all()
    product_count=Product.objects.all().count()
    pageinator=Paginator(product_list,8)#生产paginator对象，设置每页8条数据
    page=request.GET.get('page',1)#获取当前的页码，默认为第一页
    currentPage=int(page)
    try:
        product_list=pageinator.page(page)
    except PageNotAnInteger:
        product_list=pageinator.page(1)
    except EmptyPage:
        product_list=pageinator.page(pageinator.num_pages)
    print(product_list,file=doc)
    return render(request,'product_manage.html',{"user":username,'products':product_list})



#搜索功能
@login_required
def productsearch(request):
    username=request.session.get('user','')
    search_productname=request.GET.get("apitestname",'')
    product_list=Product.objects.filter(productname__icontains=search_productname)
    return render(request,'product_manage.html',{"user":username,"apitests":product_list})



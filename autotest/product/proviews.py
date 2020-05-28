from django.shortcuts import render
from product.models import Product
# Create your views here.

#产品管理
def product_manage(request):
    doc = open("test.log", "a+")
    username=request.session.get('user','')
    product_list=Product.objects.all()
    print(product_list,file=doc)
    return render(request,'product_manage.html',{"user":username,'products':product_list})

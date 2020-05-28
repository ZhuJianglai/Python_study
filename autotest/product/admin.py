from django.contrib import admin
from product.models import Product
from apitest.models import Apitest,Apistep,Apis
# Register your models here.

class ProdauctAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','create_time','id']
    inlines = [Apitest]

class ApiAdmin(admin.TabularInline):
    list_disolay=['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']
    model = Apis
    extra = 1

admin.site.register(Product)  #把产品模块注册到Django admin中并显示

from django.contrib import admin
from webtest.models import Webcase,Webcasestep
# Register your models here.

class WebcasestepAdmin(admin.TabularInline):
    list_display=['webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod','webtestdata','webassertdata','webtestresult','create_time','id','webcase']
    model = Webcasestep
    extra = 1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename','webtestresult','webtester','create_time','id']
    inlines =[WebcasestepAdmin]


admin.site.register(Webcase,WebcaseAdmin)
admin.site.register(Webcasestep)
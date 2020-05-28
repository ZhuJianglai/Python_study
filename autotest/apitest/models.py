from product.models import Product
from django.db import models

# Create your models here.
#流程接口表
class Apitest(models.Model):
    #关联产品的ID，其中product是应用名，Product是product应用的表名
    Product =models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    apitestname=models.CharField('流程接口名称',max_length=60) #流程接口测试场景
    apitestdesc=models.CharField('描述',max_length=64,null=True) #流程接口描述
    apitester=models.CharField('测试负责人',max_length=16)#执行人
    apitestresult=models.BooleanField('测试结果')#流程接口测试结果
    create_time=models.DateTimeField('创建时间',auto_now=True)#自动获取当前时间未创建时间
    class Meta:
        verbose_name='流程场景接口'
        verbose_name_plural='流程场景接口'
    def __str__(self):
        return self.apitestname

class Apistep(models.Model):
    Apitest=models.ForeignKey(Apitest,on_delete=models.CASCADE,) #关联接口ID
    apiname=models.CharField('接口名称',max_length=100) #接口标题
    apiurl=models.CharField('url地址',max_length=200)#url地址
    apiparamvalue=models.CharField('请求参数和值',max_length=800)#参数值
    REQUEST_METHOD=(('get','get'),('post','post'),('put','put'),('delete','delete'),('patch','patch'))
    apimethod=models.CharField(verbose_name='请求方式',choices=REQUEST_METHOD,default='get',max_length=200,null=True)#请求方式
    apiresult=models.CharField('预期结果',max_length=200)#预期结果
    apiresponse=models.CharField('响应数据',max_length=5000,null=True)
    apistatus=models.BooleanField('是否通过')#测试结果
    create_time=models.DateTimeField('创建时间',auto_now=True)#获取当前时间为创建时间
    def __str__(self):
        return self.apiname

#单一场景接口
class Apis(models.Model):
    Product =models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    apiname=models.CharField('接口名称',max_length=100)
    apiurl=models.CharField('url地址',max_length=200)
    apiparamvalue=models.CharField('请求参数和值',max_length=800)#参数值
    REQUEST_METHOD=(('0','get'),('1','post'),('2','put'),('3','delete'),('4','patch'))
    apimethod=models.CharField(verbose_name='请求方式',choices=REQUEST_METHOD,default='get',max_length=200,null=True)#请求方式
    apiresult=models.CharField('预期结果',max_length=200)#预期结果
    apistatus=models.BooleanField('是否通过')#测试结果
    create_time=models.DateTimeField('创建时间',auto_now=True)#获取当前时间为创建时间
    class Meta:
        verbose_name='单一场景接口'
        verbose_name_plural='单一场景接口'
    def __str__(self):
        return self.apiname
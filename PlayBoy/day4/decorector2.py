# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-



import time
def timer(func): #timer(test1)  func=test1
    #def deco():
    def deco(*args,**kwargs):  #当需要各种参数的额时候，使用*args,**kwargs
        start_time=time.time()
        func(*args,**kwargs)
        stop_time =time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return deco



# def timer():
#     def deco():
#         pass
#

#装饰器的使用
@timer  #test1=timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")


@timer
def test2(name,age):      #test2=timer(test2)  ==deco     test2()=deco()
    time.sleep(3)
    print("in the test2",name,age)

#test1() #--->deco
test1()
test2('zhu',28)
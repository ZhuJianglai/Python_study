# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-。

# 装饰器高阶函数
#A:把一个函数名当做实参传给另外一个函数（在不修改被装饰函数源代码的情况下为 器添加功能）
import  time
def bar():
    time.sleep(1)
    print("in the bar")


def test(func):
    start_time=time.time()
    func()   #运行bar
    stop_time=time.time()
    print("the func run time is %s"%(stop_time-start_time))
print("------------------1--------------")
test(bar)



# B: 返回值中包含函数名

def test1(func):
    print(func)
    return func  #返回内存地址
print(test1(bar))  #将内存地址传给test1
print("------------------2--------------")
bar=test1(bar)   #
bar()  # run bar  调用没有被改变



# 嵌套函数,在一个函数内再def定义一个函数
def foo():
    print("in the foo")
    def test3():
        print("in the test")
    test3()
print("------------------3--------------")
foo()



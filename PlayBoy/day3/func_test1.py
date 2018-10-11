# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

#过程 :又返回值的函数
def func1():
    print("in the func1")
    return 0

#函数
def func2():
    print("in the func2")

def func3():
    print("this is return func1")
    return func1()    #可以返回一个函数



x=func1()
y=func2()

print("func1 return %s" %x)
print("func2 return %s" %y)

func3()


def test(x,y):
    print(x)
    print(y)


test(1,2) #位置参数调用,与形式一一对应
print("-------------------------------")
test(y=5,x=6) #位置参数调用，与型参顺序无关
test(8,y=6)



def test1(x,y=2): #默认参数:调用的是默认的参数非必须传递，传递默认值，例如sql的端口号
    print(x)
    print("-------------------------------")
    print(y)
test1(1)
test1(1,5)


# 参数组,参数名称前加*并用args,  接受位置参数
def test_1(*args):
    print(args)
test_1(1,2,3,4,5)
test_1(*[1,2,3])


def test_2(x,*args):
    print(x)
    print(args)
test_2(1,2,3,4,5)

#**kwargs，把N个关键字参数转换为字典
def test_3(**kwargs):
    print(kwargs)
    print(kwargs['name'])
test_3(name='zhu',age=8,sex='f')
test_3(**{'name':'zhu','age':8,'sex':'f'})

def test_4(name,**kwargs):
    print(name)
    print(kwargs)
test_4('zhu',age=18)




def test_5(name,age=18,**kwargs):
    print(name)
    print(kwargs)
test_5('zhu',age=18)


def test_5(name,*args,**kwargs):
    print(name)
    print(args)
    print(kwargs)
test_5('zhu',('1','2'),age=18)


















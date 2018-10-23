# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-
#斐波那契

def fib(max):
    n,a,b=0,0,1
    while n <max:
        # print(b)
        yield b   #yied 返回当前状态的值
        a,b=b,a+b
        n=n+1
    return 'done'


f=fib(10)
print(f)
# print(f.__next__())
print("=========start loop=====")
for i in f:
    try:
        print(i)
    except StopIteration as e:
        print('Genenrator return value:',e.value)



for i in range(10):
    print(f.__next__())



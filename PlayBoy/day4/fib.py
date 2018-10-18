# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-
#斐波那契

def fib(max):
    n,a,b=0,0,1
    while n <max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'


fib(10)

1

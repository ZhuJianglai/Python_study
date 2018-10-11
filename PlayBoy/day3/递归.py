# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-



#递归函数
def calc1(n):
    print(n)
    if int(n/2)>0:
        return calc1(int(n/2))
    print("-->",n)

    calc1(50)
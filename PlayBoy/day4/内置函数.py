# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-


#内置函数
#参考说明https://docs.python.org/3.7/library/functions.html
print(all([1,-1,3]))
print(any([]))
print(bin(2)) #将数字转换二进制
print(chr(99))   #将ascii值转换成字符
compile  #将代码编译后配合exec执行
dir() #查询函数的方法
divmod(5,2)  #5除以2
calc= lambda n:print(n)  #匿名函数
calc(5)

res=filter(lambda n:n>50,range(70)) #filter 过滤，可配合lambda使用
for i in res:
    print(i)
    print("----")

res=map(lambda n:n*n,range(10))
res1=[lambda i:i*2 for i in range(10)]
for i in res:
    print(i)
    print("----")



#累加
import functools
res2=functools.reduce(lambda x,y:x+y,range(100))
print(res2)

#----------
print(globals())  #将程序中的关键字以KEY   veule显示出来

hash("alxe") #将对应的字符串转换（映射）成一个数字串，可进行排序，对半查找
hex(8)#将数字转换成16进制

a={6:3,8:22,12:3,1:343}
# sorted
print(sorted(a.items()))  #将无序字典按key排序
print(sorted(a.items(),key=lambda x:[1] )) #将无序字典按velue排序

a=[1,2,3,4,5]
b=['a','b','c','d']
for i in zip(a,b):  #将列表组合起来，按最少的组合
    print(i)

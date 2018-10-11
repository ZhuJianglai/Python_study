# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-
import copy

names=['zhu','yang','wu','zheng',['haha','laowang'],'wang','zhao','qian']
# names.append('han')   #追加
# names.insert(2,'xv')  #插入
names1=names.copy()
names[2]='WU'
names[4][1]='zhujianglai'
print(names)
print(names1)
names2=copy.deepcopy(names)
names[2]='WU'
names[4][1]='zhujianglai'
print(names)
print(names2)
# print(names[0])
# print(names[:2])
# print(names[1:3]) #切片
# print(names[-1]) #切片
# print(names[-3:])#切片
#


# 删除
# names.remove('qian')
# print(names)
# del names[3]
# print(names)
# names.pop()
# print(names)


# print(names.index('wu'))
# names.reverse()
# print(names)
# names.sort()
# print(names)





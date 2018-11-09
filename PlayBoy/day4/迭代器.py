# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

#首先获得Iterator对象
it=iter([1,2,3,4,5])
#循环
while True:
    try:
        #获取下一个值
        x = next(it)
    except StopIteration:
        #遇到StopIteration停止
        break
# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-
import time
def consumer(name):
    print("%s 准备吃包子啦！"%name )
    while True:
        baozhi=yield
        print("包子[%s]来啦，被[%s]吃了！"%(baozhi,name))
c=consumer("xiaozhu")
c.__next__()


def producer(name):
    c=consumer("A")
    c2=consumer("B")
    c.__next__()
    c2.__next__()
    print("我要开始做包子拉")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子分成了两半")
        c.send(i)
        c2.send(i)
producer("alex")
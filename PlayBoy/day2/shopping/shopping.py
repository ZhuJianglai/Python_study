# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-



def rshopinfo(path):
    file=open(path,'r')
    filelines=file.readline()
    while True:
        for i in filelines:
            print(i)
            filelines=file.readline()

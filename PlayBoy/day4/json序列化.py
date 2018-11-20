# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

#json序列化
import json
import pickle

def hello(name):
    print(name)


info={
    "name":"zhu",
    "age":22,
}

info1={
    "name":"zhu",
    "age":22,
    "func":hello
}
f=open("txt.txt","w")
f.write(json.dumps(info))
f.close()


f=open("txt1.txt","w")
f.write(pickle.dumps(info1))
f.close()



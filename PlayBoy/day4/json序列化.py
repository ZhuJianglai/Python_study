# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

#json序列化
import json
info={
    "name":"zhu",
    "age":22
}

f=open("txt.txt","w")
f.write(json.dumps(info))
f.close()
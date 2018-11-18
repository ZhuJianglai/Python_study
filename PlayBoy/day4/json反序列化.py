# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

#json反序列化

import json
f=open("txt.txt","r")
date=json.loads(f.read())
print(date["age"])

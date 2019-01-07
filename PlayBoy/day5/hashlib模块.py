# -*- coding: utf-8 -*-
# @Time    : 2019-1-7 18:55
# @Author  : 081191
# @FileName: hashlib模块.py
# @Software: PyCharm

import hashlib

m=hashlib.md5()
m.update(b'hello')
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())   #helloIt's me

m2=hashlib.md5()
m.update(b"helloIt's me")
print(m.hexdigest())

m2=hashlib.sha384
m.update(b"helloIt's me")
print(m.hexdigest())
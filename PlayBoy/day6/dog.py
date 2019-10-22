# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-


#面向对象
class Dog:  #定义类
    def __init__(self,name):
        self.name=name

    def bulk(self):
        print("%s: wang wang wang"%self.name)



d1=Dog("小狗")
d2=Dog("大狗")


d1.bulk()
d2.bulk()

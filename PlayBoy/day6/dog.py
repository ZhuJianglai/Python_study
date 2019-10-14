# -*- coding: utf-8 -*-
# @Time    : 2019-1-17 20:05
# @Author  : 081191
# @FileName: dog.py
# @Software: PyCharm

#类
class Dog:
    def __int__(self,name):
        self.name=name

    def bulk(self):
        print("%s wang  wang  wang" %self.name)



d1=Dog("陈荣华")  #制作狗一
d2=Dog("hahaha")  #制作狗2
d3=Dog("ruoruo")  #制作狗3
d1.bulk()
d2.bulk()
d3.bulk()


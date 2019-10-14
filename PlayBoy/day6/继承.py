# -*- coding: utf-8 -*-
# @Time    : 2019-1-23 19:54
# @Author  : 081191
# @FileName: 继承.py
# @Software: PyCharm

class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print("%s  is eating.."% self.name)


    def watering(self):
        print("%s  is watering.." % self.name)

class Man(people):
    def piao(self):
        print("%s  is piaoing.." % self.name)



class Weman:
    def got_birth(self):
        print("%s is boring baby"%self.name)



men1=people("wang",22)
men1.eat()

men2=Man("li",23)
men1.piao()


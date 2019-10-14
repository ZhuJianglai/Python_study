# -*- coding: utf-8 -*-
# @Time    : 2019-1-21 19:15
# @Author  : 081191
# @FileName: cs pllay.py
# @Software: PyCharm



class Role:
    n=123 #类变量
    name='我是类变量'      #先找实例变量，再找类变量；类变量即大家共有的熟悉，可节约开销
   # n_list=[]
    def __init__(self,name,weapon,life_value=100,money=15000):
        #构造函数
        #在实例化时做一些类的初始化的工作
        self.name=name    # r1.name=name 实例变量（静态属性），作用域就是实例本身
        self.weapon=weapon
        self.life_value=life_value
        self.__life_value = life_value   #变成是有属性
        self.money=money


    def __del__(self):  # 在实例释放、销毁的时候执行，通常用于一些收尾工作
        print("%s ,the end"%self.name)

    def shot(self):#类的方法，功能（动态属性）
        print("shoting...")

    def got_shot(self):
        self.__life_value -= 50
        print("%s, ah ...i got shot..."%self.name)

    def by_gun(self,gun_name):
        print("%s just bought %s"%(self.name,gun_name))

    def __by_gun(self,gun_name):  #在前面加__变成私有
        print("%s just bought %s"%(self.name,gun_name))

    def status(self):
        print("name:%s,gunname:%s,life_value:%d"%(self.name,
                                                        self.weapon,
                                                  self.__life_value))
# print(Role)


r1=Role('wang','b22')  # Role(r1,'wang,b22) 生成一个角色，把一个类变成一个具体的对象的过程叫   实例化（初始化）
r1.got_shot()   #Role.got_shot(r1)
print(r1.status())
#r1.n_list.append("from r1")


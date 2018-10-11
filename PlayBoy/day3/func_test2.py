# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

# # 全局变量
# school="wanhe"


# # 局部变量:只在函数中生效
# def change_name(name):
#     global  school
#     school = "old wanhe"
#     print("before change",name,school)
#     name='yangqing'  #这个函数就是这个变量的作用域（这里就是局部变量）
#     print("after change",name)
#
# name='zhu'
# change_name(name)
# print(name)


names=["zhu","yang","ning","qing"]
def change_name():
    print("before change", names)
    names[0]='yangqing'  #这个函数就是这个变量的作用域（这里就是局部变量）
    print("after change",names)


change_name()


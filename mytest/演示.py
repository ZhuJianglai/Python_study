# -*- coding: utf-8 -*-
# @Time    : 2019-07-22 11:48
# @Author  : 081191
# @FileName: 演示.py
# @Software: PyCharm


import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Kahn Software v1")  # #窗口标题
win.geometry("500x300+200+20")  # #窗口位置500后面是字母x

'''
下拉菜单
'''
xVariable = tkinter.StringVar()  # #创建变量，便于取值

com = ttk.Combobox(win, textvariable=xVariable)  # #创建下拉菜单
com.pack()  # #将下拉菜单绑定到窗体
list = ["河北", "河南", "山东"]
print(tuple(list))
com["value"] = tuple(list) # #给下拉菜单设定值
com.current(2)  # #设定下拉菜单的默认值为第3个，即山东


def xFunc(event):
    print(com.get()+"is check")  # #获取选中的值方法1
    # print(xVariable.get())  # #获取选中的值方法2


com.bind("<<ComboboxSelected>>", xFunc)  # #给下拉菜单绑定事件


win.mainloop()
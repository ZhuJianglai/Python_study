# -*- coding: utf-8 -*-
# @Time    : 2019-07-18 11:52
# @Author  : 081191
# @FileName: GUI_test.py
# @Software: PyCharm

from mytest import list_file as listfilename
import tkinter
from tkinter import ttk
from tkinter import *  # 导入 Tkinter 库

file_path="E:\朱宁文件\项目文件\热水器\电热水器\固件//130B\固件日志" #目录地址
root = tkinter.Tk()  # 创建窗口对象的背景色
# 创建两个列表


# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
li = listfilename.file_name(file_path)
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)

comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist=ttk.Combobox(root,textvariable=comvalue) #初始化
comboxlist["values"]=tuple(li)
comboxlist.current(0)  #选择第一个
comboxlist.bind("<<ComboboxSelected>>")  #绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.pack()

for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()




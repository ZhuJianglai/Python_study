# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

#字符串方法

name='zhu-yang'
print(name.capitalize())  #首字母
print(name.count("u")) #统计字符
print(name.center(50,"*"))   #打印50个字符，不足以*

#字典
info ={'01':'zhu','02':'yang'}
print(info['02'])
print(info.get('02'))


print('01' in info)

# 字典嵌套
info ={
    '湖北':{
        '武汉':{'武昌','汉口'},
        '宜昌':{'夷陵'}
    },
    '北京':{'01':{'昌平'},
          '02':{''},
          '03':{''}}
}

while True:
    for i in info:
        print(i)

    choice=input("选择进入1>>:")

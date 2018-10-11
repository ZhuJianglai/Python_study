# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

# f=open("for you.txt",'r').read()  #读取全部文件内容
# print(f)



# low bigger
f=open("for you.txt",'r')
for index,line in enumerate(f.readlines()):
    print(index,line)
    if index>30:
        print("---------分割--------")
        break
    f.close()



#high bigger
count=0
f1=open("for you.txt","r")
for line in f1:
    if count==9:
        print("----------------stop-----------------")
        count += 1
        continue
    print(line)
    count +=1



# 光标定位
f2=open("for you.txt","r") # 文件句柄 只读
f2=open("for you.txt","r+")  #文件句柄 读写
f2=open("for you.txt","w+")  #文件句柄 写读
f2=open("for you.txt","rb")  #文件句柄 二进制文件  网络传输只能用二进制传输
print(f2.tell())
print(f2.readline())
print(f2.readline())
print(f2.readline())
print(f2.tell())
print(f2.seek(10))
print(f2.readline())
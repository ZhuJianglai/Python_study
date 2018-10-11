# author：zhu

#输入用户名密码
#认证成功后显示欢迎信息
#输入三次后锁定,推出


def f_IO(filepath,username,password):
    f=open(filepath,'r')
    lines=f.readline()
    while lines:
        # print(lines)
        line = lines.split(',')
        if username == line[0] and password == line[1].strip():
            return True
        lines=f.readline()
    f.close()

def f_IP(filename,username,password):
    f=open(filename,'r')
    lines=f.readline()
    while lines:
        line =lines.split(',')
        if username== line[0] and password ==line[1].strip():
            return True
        lines =f.readline()
    f.close()



i=0 #初始次数
while i<3:
    username=input("username:")
    password=input("password:")
    if f_IO('username.txt',username,password) is True:
        print('''{_username},welcome!'''.format(_username=username))
        break
    elif f_IP('input.txt',username,password) == True:
        print('you have input this username!')
        break
    else:
        f = open("input.txt", "a+")
        info = '''{_username},{_password}'''.format(_username=username, _password=password)
        f.write(info + '\n')
        if i == 2:
            print("the times out")
        else:
            print("please try agoin!")
    i += 1










# i=0
# # for i in range(3):
# while i <3:
#     username = input("username:")
#     password = input("password:")
#     print(i)
#     f = open("username.txt", 'r')
# # lines =f.readline().split(",")
#     lines = f.readline()
#     while lines:
#         print(lines)
#         line = lines.split(',')
#         if username == line[0] and password == line[1].strip():
#             print("{_username},welcome!".format(_username=username))
#             break
#         else:
#             f = open("input.txt", "a+")
#             info = '''{_username},{_password}'''.format(_username=username, _password=password)
#             f.write(info + '\n')
#             if i == 2:
#                 print("the times out")
#             else:
#                 print("please try agoin!")
#                 print(line)
#             lines=f.readline()
#     f.close()
#     i +=1
#
#


# for i in range(3):
#     print(i)
#     username = input("username:")
#     password = input("password:")
#     if username ==lines[0] and password==lines[1]:
#         print("{_username},welcome!".format(_username=username))
#         break
#     else:
#         f=open("input.txt","a+")
#         info='''{_username},{_password}'''.format(_username=username,_password=password)
#         f.write(info+'\n')
#         if i==2:
#             print("the times out")
#         else:
#             print("please try agoin!")


# username1=lines[0]
# password1=lines[1]
# print(lines)
# print(username1)
# print(password1)
# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 10:46
# @Author  : 081191
# @FileName: sendEmail.py
# @Software: PyCharm

# !/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import datetime
import glob
import time
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import re
import ast
import difflib
'''difflib是python 自带的一个方法
返回的结果是个list
返回的list元素数量是可控的,
cutoff参数是0到1的浮点数, 可以调试模糊匹配的精度,一般为0.6就可以了, 1为精确匹配,'''


_smtp_server = 'smtp.qq.com'
path_list = [["E://OTA//new_lib_sign",'Q6'],["E://OTA//lib_sign",'Q6'],['E://OTA//Q6_1#','Q6']]  #日志目录
filename_dic={}

# 获取最新的文件
def file_neme(file_path):
    time_name = (datetime.date.today() + datetime.timedelta(-1)).strftime('%Y%m%d')
    os.chdir(file_path)
    # print(os.chdir(file_path))
    for logname in glob.glob("UartLog_" + time_name + ".log"):
        if logname == None:
            return '没有日志'
        else:
            return logname


def sendEmail(sender, sender_password, receiver):
    doc = open("E://OTA//new_lib_sign//send.log", "a+")

    i=0
    filename_dic=filename_list(path_list)
    print(filename_dic,file=doc)

    print("*" * 17 + "start send email" + "*" * 17, file=doc)
    print(str(datetime.datetime.now()) + "starting create Email infomation!!", file=doc)
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Q3_Q6TestTeam", 'utf-8')
    message['To'] = Header("wifi测试", 'utf-8')
    subject = 'Q3_Q6测试日志记录'
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText(
        'Q3_Q6日志情况:'+str(filename_dic),
        'plain', 'utf-8'))
    num = 0
    for key in filename_dic:
        filename=filename_dic[key]
        path=ast.literal_eval(key)[0]#将字符串转换成list
        print(filename == 'No log file was found')
        print(filename != 'discontent'and filename != 'No log file was found')
        if filename == 'discontent':
            num +=1
        elif filename != 'discontent'and filename != 'No log file was found':
            print(str(datetime.datetime.now()) + "search Mail attachment", file=doc)
            att1 = MIMEText(open(path + "\\" + filename, 'rb').read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            print(str(datetime.datetime.now()) + "add Mail attachment"+key +':'+ filename, file=doc)
            att1.add_header("Content-Disposition", "attachment", filename=("utf-8", "", key +':'+ filename))
            message.attach(att1)
    if num == filename_dic.__len__():
        print('These logs do not need to be send!',file=doc)
        print("*" * 50, file=doc)
        print("*" * 50, file=doc)
        exit()

    try:
        print(str(datetime.datetime.now()) + "Link Mailbox Server!!", file=doc)
        smtpObj = smtplib.SMTP(_smtp_server, 587)
        smtpObj.starttls()
        # smtpObj.set_debuglevel(1)
        print(str(datetime.datetime.now()) + "Login Mailbox Server!!", file=doc)
        smtpObj.login(sender, sender_password)
        print(str(datetime.datetime.now()) + ":start sending...", file=doc)
        receivers = receiver.split(",")
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print(str(datetime.datetime.now()) + ":send Email success!", file=doc)

    except Exception as e:
        print(str(datetime.datetime.now()) + ":Error:send Email failure!,Error info:" + str(e), file=doc)
        print("one minites later send agin!",file=doc)
        sleep(60)
        sendEmail('554910034@qq.com', 'bcjaxhfbwguxbfbg', '316967266@qq.com,345022596@qq.com')

    print("*" * 50, file=doc)
    print("*" * 50, file=doc)
    doc.close

str1 = 'connect push server success'
str3='Auto clean text'


def filename_list(filepath):
    i = 0  #路径
    for i in range(len(path_list)):
        file_path = path_list[i][0]
        file_type =path_list[i][1]
        filename = file_neme(file_path)
        con_Q3_num = 0
        con_Q6_num=0
        con_Q6_num1 = 0

        if filename is not None:
            lin_num=len(open(file_path + "\\" + filename, 'r').readlines())
            file_to_read = open(file_path + "\\" + filename, 'r')
            finally_txt = file_to_read.readlines()[lin_num - 5:]
            is_str=difflib.get_close_matches(str3, finally_txt, 1, cutoff=0)
            if is_str.__len__()==1:
                path_list[i].append("串口日志收集出问题啦")
                filename_dic[str(path_list[i])] = filename
                print(path_list[i])
            else:
                for line in open(file_path + "\\" + filename, 'r').readlines():
                    if file_type =='Q3' and str1 in line:
                        con_Q3_num +=1
                    if file_type =='Q6':
                        str2 = re.search(r'\{(.*)登录成功(.*)}', line)
                        # print(str2)
                        if str2 is not None:
                            con_Q6_num += 1
                            str2_dic = eval(str2.group())
                            log_time = time.mktime(time.strptime(str2_dic['Time'], "%Y-%m-%d %H:%M:%S"))
                            time_name = (datetime.date.today() + datetime.timedelta(-1)).strftime('%Y-%m-%d')
                            start_time = time.mktime(time.strptime(time_name + ' 04:00:00', "%Y-%m-%d %H:%M:%S"))
                            end_time = time.mktime(time.strptime(time_name + ' 05:00:00', "%Y-%m-%d %H:%M:%S"))
                            if log_time > start_time and log_time < end_time:
                                con_Q6_num1 += 1
                if con_Q6_num1>1:
                    path_list[i].append(con_Q6_num1)
                    filename_dic[str(path_list[i])] = filename
                elif con_Q6_num1==1 and con_Q6_num-con_Q6_num1>0:
                    path_list[i].append(con_Q6_num)
                    filename_dic[str(path_list[i])] = filename
                if con_Q3_num>0:
                    path_list[i].append(con_Q3_num)
                    filename_dic[str(path_list[i])] = filename
                else:
                    filename_dic[str(path_list[i])] = 'discontent'
        else:
            filename_dic[str(path_list[i])] = 'No log file was found'
    return filename_dic



if __name__ == "__main__":
    sendEmail('554910034@qq.com', 'bcjaxhfbwguxbfbg', '316967266@qq.com')


# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 10:46
# @Author  : 081191
# @FileName: sendEmail.py
# @Software: PyCharm

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

file_path="C:\Users\Administrator\Desktop\wifi_log_tool" #目录地址

# 获取最新的文件
def file_neme(file_path):
    lists = os.listdir(file_path)                                    #列出目录的下所有文件和文件夹保存到lists
    # print(lists)
    lists.sort(key=lambda fn:os.path.getmtime(file_path + "\\" + fn),reverse=True)#按时间排序
    # print(lists)
    # file_new = os.path.join(file_path,lists[0])                     #获取最新的文件保存到file_new
    # print(file_new)
    # print(lists[1])
    return lists[1]

def sendEmail(sender,sender_password,receivers):
    # sender = '554910034@qq.com'
    # sender_password = 'bcjaxhfbwguxbfbg'
    # receivers = ['316967266@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'

    #获取要添加附件的文件
    filename=file_neme(file_path)



    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Q6_TestTeam", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Q6测试日志记录'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('Q6测试固件日志记录……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_path+"\\"+filename, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename=%s'%filename
    message.attach(att1)


    try:
        smtpObj = smtplib.SMTP(smtp_server, 587)
        smtpObj.starttls()
        # smtpObj.set_debuglevel(1)
        smtpObj.login(sender, sender_password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print( "邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



if __name__ == "__main__":
    sendEmail('554910034@qq.com','bcjaxhfbwguxbfbg','316967266@qq.com')




# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 10:46
# @Author  : 081191
# @FileName: sendEmail.py
# @Software: PyCharm

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import os
import datetime
import glob

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

file_path="C://Users\Administrator\Desktop\Q6_125_com17" #目录地址

# 获取最新的文件
def file_neme(file_path):
    time_name=(datetime.date.today()+datetime.timedelta(-1)).strftime('%Y%m%d')
    os.chdir(file_path)
    for logname in glob.glob("UartLog_"+time_name+".log"):
        return logname


def sendEmail(sender,sender_password,receivers):
    
    doc=open("1.log","w")
    # sender = '554910034@qq.com'
    # sender_password = 'bcjaxhfbwguxbfbg'
    # receivers = ['316967266@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'

    #获取要添加附件的文件
    filename=file_neme(file_path)
    print(str(datetime.datetime.now())+"attachment name:"+filename,file=doc)

    print(str(datetime.datetime.now())+"starting create Email infomation!!",file=doc)
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Q6_TestTeam", 'utf-8')
    message['To'] = Header("wifi测试", 'utf-8')
    subject = 'Q6测试日志记录'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('Q6测试固件日志记录:体验楼Q6-125-B,com17_Q6_125_v1.2.7_B:%s'%filename, 'plain', 'utf-8'))

    print(str(datetime.datetime.now())+"search Mail attachment",file=doc)
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_path+"\\"+filename, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字,这里是非中文的写发
    # att1["Content-Disposition"] = 'attachment; filename=%s'%filename
    
    print(str(datetime.datetime.now())+"add Mail attachment",file=doc)
    # 以下是中文附件名称的写法
    att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "体验楼Q6-125-B日志：%s"%filename))
    message.attach(att1)


    try:
        print(str(datetime.datetime.now())+"Link Mailbox Server!!",file=doc)
        smtpObj = smtplib.SMTP(smtp_server, 587)
        smtpObj.starttls()
        # smtpObj.set_debuglevel(1)
        print(str(datetime.datetime.now())+"Login Mailbox Server!!",file=doc)
        smtpObj.login(sender, sender_password)
        print("*"*20+"send email"+"*"*20,file=doc)
        print(str(datetime.datetime.now())+":sending...",file=doc)
        # print(filename)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print(str(datetime.datetime.now())+":send Email success!",file=doc)
        print("*"*50,file=doc)
    except Exception as e:
        print(str(datetime.datetime.now())+":Error:send Email failure!Error info:"+str(e))

    doc.close
    


if __name__ == "__main__":
    sendEmail('554910034@qq.com','bcjaxhfbwguxbfbg','316967266@qq.com')




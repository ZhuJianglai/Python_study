# -*- coding: utf-8 -*-
# @Time    : 2019-03-12 10:46
# @Author  : 081191
# @FileName: sendEmail.py
# @Software: PyCharm

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import os
import mytest.listFilename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
def sendEmail(sender,sender_password,receivers):
    # sender = '554910034@qq.com'
    # sender_password = 'bcjaxhfbwguxbfbg'
    # receivers = ['316967266@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("Q6_TestTeam", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Q6测试日志记录'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    message.attach(att1)


    try:
        smtpObj = smtplib.SMTP(smtp_server, 587)
        smtpObj.starttls()
        smtpObj.set_debuglevel(1)
        smtpObj.login(sender, sender_password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print( "邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")



if __name__ == "__main__":
    sendEmail('554910034@qq.com','bcjaxhfbwguxbfbg','316967266@qq.com')




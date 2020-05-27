# -*- coding: utf-8 -*-
# @Time    : 2019-03-22 11:41
# @Author  : 081191
# @FileName: 3.py
# @Software: PyCharm


# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 11:34
# @Author  : 081191
# @FileName: 分析日志.py
# @Software: PyCharm
import pandas as pd
txt_str="Cmode"
# num = 1
a = list()
title = [U'时间', U'当前温度', U'上一次温度', U'模块内部时间', U'Suc']  # 表格title
def read_txt_high(filename):

    file_to_read=open(filename, 'r')
    for line in file_to_read.readlines():
        if txt_str in line:
            temp_list = line.replace('] -/:', '').replace('[', '').replace('\n', '').split(",")
            print(temp_list)
            print(10*"*")
            if temp_list.__len__()==5:
                temp_list[0] = temp_list[0].replace(' Cmode=7', '')
                temp_list[1] = temp_list[1].replace('WIn=', '')
                temp_list[2] = temp_list[2].replace('Last=', '')
                temp_list[3] = temp_list[3].replace('T=', '')
                temp_list[4] = temp_list[4].replace('Suc=', '')
                # print(temp_list)
                a.append(temp_list)
            else:
                a.append(temp_list)
            print(temp_list)
            # break

    # print(a)

    test = pd.DataFrame(columns=title, data=a)
    # test.to_csv('e:/testcsv.csv', encoding='gbk')
    test.to_csv(filename+'.csv', encoding='gbk')

    # while True:
    #     lines = file_to_read.readline()  # 整行读取数据
    #     if txt_str in lines:
    #         line=lines
    #         global num
    #         num=int(num)+1
    #         print(type(num))
    #         print(line)
    #         time_str=re.findall(r'\[.+\]',line,re.S)
    #         if time_str.__len__()==1:
    #             time_str1=time_str[0]
    #         else:
    #             time_str1="******"
    #         print(time_str1)
    #         win = re.findall(r'WIn=\d*',line,re.S)
    #         if win.__len__()==1:
    #             win1=win[0].strip("WIn=")
    #         else:
    #             win1="xx"
    #         print(win1)
    #         last = re.findall(r'Last=\d*', line, re.S)
    #         if last.__len__()==1:
    #             last1=last[0].strip("Last=")
    #         else:
    #             last1="xx"
    #         print(last1)
    #         int1=re.findall(r'\d+', line, re.S)
    #         print(int1)
    #         workbook = xlsxwriter.Workbook('d:\kami1.xlsx')  # 创建一个Excel文件
    #         worksheet = workbook.add_worksheet("123456")  # 创建一个sheet
    #         title = [U'时间', U'当前温度', U'上一次温度', U'模块内部时间', U'Suc']  # 表格title
    #         worksheet.write_row('A1', title)
    #         data = [time_str1,win1,last1]
    #         row = 'A' + str(num)
    #         worksheet.write_row(row,data)
    #         # f = open("UartLog_20190310.log.txt", "a+")
    #         # if int(last)-int(win)>2:
    #         # f = open("UartLog_20190312_1.log.txt", "a+")
    #         # f.write(line+'\n')
    #         # print("--")
    #         # f.close()
    #         workbook.close()


if __name__ == '__main__':
    read_txt_high("UartLog_20190320.log")
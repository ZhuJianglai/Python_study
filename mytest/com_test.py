# -*- coding: utf-8 -*-
# @Time    : 2019-07-16 17:51
# @Author  : 081191
# @FileName: com_test.py
# @Software: PyCharm

#
# import serial
# import os
# from time import sleep
# if __name__ == '__main__':
#     serial = serial.Serial('/dev/ttyUSB0', 9600,timeout = 3600)
#     if serial.isOpen() :
#         print("open success")
#     else:
#         print("open failed")
#     while True:
#         send_data = input("input a data: ")
#         send_data = send_data + '\r\n'
#         serial.write(send_data.encode())
#         data=serial.read(1)#阻塞读直到读出第一个数据，然后用serial.inWaiting()计算出接收缓冲区还有多少个数据，使用read读出来
#         sleep(0.1) #有些AT指令的回复太长，延迟一段时间，希望开发板的串口已经将AT指令的回复已经全部接收到缓冲区
#         data = (data + serial.read(serial.inWaiting())).decode()
#         print(data)
#



##模块为Pyserial

import serial

import serial.tools.list_ports

import time

#####list serial ports####

port_list = list(serial.tools.list_ports.comports())

for port in port_list:

    print(port[0])

######Read AI data####

ser = serial.Serial("COM22",9600,timeout=0.5)

time.sleep(3)

ser.write("read\n".encode())

time.sleep(0.5)

print(ser.read(50).decode('gbk'))

ser.close

#####################

# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 15:33
# @Author  : 081191
# @FileName: time.py
# @Software: PyCharm


from datetime import datetime

times = datetime.now().strftime("%Y%m%d%H%M%S")
times1 = int(datetime.now().strftime("%H%M%S"))
print(datetime.now().strftime("%Y%m%d%H%M%S"))
print(times1)


if times1 in range(153800,153942):
    print("times is ok")

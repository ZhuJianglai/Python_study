# -*- coding: utf-8 -*-
# @Time    : 2019-03-11 15:32
# @Author  : 081191
# @FileName: 1.py
# @Software: PyCharm
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()





import datetime
i = datetime.datetime.now()
print(i)
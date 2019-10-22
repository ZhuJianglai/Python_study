# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 8:34
# @Author  : 081191
# @FileName: network.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

import subprocess
from datetime import datetime
import re
import time




def ping(url):
    while True:
        p = subprocess.Popen(url, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        times = datetime.now()
        print("*"*20 + "network test,"+str(times) + "*"*20)
        inTxt("*"*20 + "network test,"+str(times) + "*"*20)

        sumcount = 0
        latecount = 0
        losscount = 0

        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            sumcount = sumcount+1
            # print(sumcount)
            if line:
                s1 = str(line, encoding='GBK')
                str1 = re.search(r'\d{1,}ms', s1)
                # print("--------"+str(datetime.now()) + ':' + s1)
                if str1 is not None:
                    if int(str1.group().replace('ms','')) > 100:
                        # print(str1.group())
                        inTxt(str(datetime.now()) + ':' +s1)
                        print(str(datetime.now()) + ':' + s1)
                        latecount =latecount+1
                else:
                    inTxt(str(datetime.now()) + ':' + s1)
                    print(str(datetime.now())+':'+s1 )
                    losscount=losscount+1
            if time.strftime("%H:%M:%S", time.localtime()) == time.strftime("%H", time.localtime())+":59:59":
                lateproportion='percent: {:.2%}'.format(latecount/sumcount)
                losscount1=losscount-1
                lossproportion='percent: {:.2%}'.format(losscount1/sumcount)

                info = "**************数据包总数：%d;延时大于100ms数量：%d,所占比例：%s;超时数量：%d,超时所占比例：%s******************"%(sumcount,latecount,lateproportion,losscount1,lossproportion)
                inTxt(info)
                print(info)
                sumcount = 0
                latecount = 0
                losscount = 0


def inTxt(txt):
    name = "network"+ str(datetime.now().strftime("%Y%m%d"))+ ".log"
    with open(name,'a+') as file:
        file.write(txt+'\n')
    file.close()


if __name__ == '__main__':
    ping('ping rubyapi.vanwardsmart.com -t')

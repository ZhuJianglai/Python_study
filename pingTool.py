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
            print(sumcount)
            if line:
                s1 = str(line, encoding='GBK')
                str1 = re.search(r'\d{1,}ms', s1)
                print("--------"+str(datetime.now()) + ':' + s1)

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
            if time.strftime("%H:%M:%S", time.localtime()) == "17:38:00":
                badcount=(latecount+losscount)
                badproportion='percent: {:.2%}'.format(badcount/sumcount)
                lateproportion='percent: {:.2%}'.format(latecount/sumcount)
                lossproportion='percent: {:.2%}'.format(losscount/sumcount)
                info="**************数据包总数："+str(sumcount)+",延时大于100ms数量："+str(latecount)+",,超时数量： "+str(losscount)
                info1="latecount:%s,超时比例：%s"%(str(latecount),str(losscount))
                print(info)
                print(info1)
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

# -*- coding: utf-8 -*-
# @Time    : 2019-07-09 8:34
# @Author  : 081191
# @FileName: network.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

import shlex
import subprocess
from datetime import datetime
from time import sleep
import re


def ping(url,sleeptime):
    while True:
        # shell_cmd = 'ping www.baidu.com'
        # url = 'www.baidu.com'
        # cmd = shlex.split(shell_cmd)
        p = subprocess.Popen(url, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # p = subprocess.Popen(['ping.exe',url], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        times = datetime.now()
        print("*"*20 + "network test,"+str(times) + "*"*20)
        inTxt("*"*20 + "network test,"+str(times) + "*"*20)
        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            if line:
                s1 = str(line, encoding='GBK')
                str1 = re.search(r'\d{1,}ms', s1)
                if str1 is not None:
                # print(type(str1))
                    if int(str1.group().replace('ms','')) > 100:
                        print(str1.group())
                        inTxt(s1)
                        print(str(datetime.now()) + ':' + s1)
                else:
                    print(str(datetime.now())+':'+s1 )
                # if str1 > '100m':
                #     inTxt(s1)
                #     print(s1)

                # tms=int(str1.repalce('ms',''))
                # print(tms)
                # s1 = str(line)
                # inTxt(s1)
                # print(s1)
        # if p.returncode == 0 :
        #     print("#"*20+'Network is ok'+"#"*20+'\n')
        #     inTxt("#"*20+'Network is ok'+"#"*20+'\n')
        # else:
        #     print("#"*20+'Network is not smooth'+"#"*20+'\n')
        #     inTxt("#"*20+'Network is not smooth'+"#"*20+'\n')
        sleep(sleeptime)




def inTxt(txt):
    name = "network"+ str(datetime.now().strftime("%Y%m%d"))+ ".log"
    with open(name,'a+') as file:
        file.write(txt+'\n')
    file.close()


if __name__ == '__main__':
    # ping('ottps.suning.com -n 5',5)
    ping('ping baidu.com -t', 5)

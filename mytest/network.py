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


def ping(url,sleeptime):
    while True:
        # shell_cmd = 'ping www.baidu.com'
        # url = 'www.baidu.com'
        # cmd = shlex.split(shell_cmd)
        p = subprocess.Popen(['ping.exe',url], shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        times = datetime.now()
        print("*"*20 + "网络测试,"+str(times) + "*"*20)
        inTxt("*"*20 + "网络测试,"+str(times) + "*"*20)
        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            if line:
                s1 = str(line, encoding='gbk')
                inTxt(s1)
                print(s1)
        if p.returncode == 0:
            print("#"*20+'Network is ok'+"#"*20+'\n')
            inTxt("#"*20+'Network is ok'+"#"*20+'\n')
        else:
            print("#"*20+'Network is not smooth'+"#"*20+'\n')
            inTxt("#"*20+'Network is not smooth'+"#"*20+'\n')
        sleep(sleeptime)




def inTxt(txt):
    # global name
    name = "network"+ str(datetime.now().strftime("%Y%m%d"))+".log"
    now_time =datetime.now().strftime("%H%M%S")
    with open(name,'a+') as file:
        file.write(txt+'\n')
    file.close()


if __name__ == '__main__':
    ping('baidu.com',10)
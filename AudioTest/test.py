# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 16:14
# @Author  : 081191
# @FileName: test.py
# @Software: PyCharm

from aip import AipSpeech
#创建三个参数
APP_ID = "16550173"
API_KEY = "HBqG3EfrQKZNIz94GC9TO3IX"
SECRET_KEY = "tIo94eUp2lklaGRYR9FLedVCSIIGEdBt"

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
#读取文件
filePath="E://python_study/audio.pcm"
with open(filePath,"rb") as fp:
    file_context=fp.read()


#识别本地文件
res=client.asr(file_context,"pcm",16000),{
    'dev_pid':1537,
}

print(res)
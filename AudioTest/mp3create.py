# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 15:04
# @Author  : 081191
# @FileName: mp3create.py
# @Software: PyCharm

from aip import AipSpeech
#创建三个参数
APP_ID = "16550173"
API_KEY = "HBqG3EfrQKZNIz94GC9TO3IX"
SECRET_KEY = "tIo94eUp2lklaGRYR9FLedVCSIIGEdBt"

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

res=client.synthesis(
    "叮咚叮咚，打开热水器",
    "zh",
    1,
    {
        "vol":5,
        "spd":4,
        "pit":8,
        "per":4
    })


#如果上面三个参数APP_ID,API_KEY,SECRET_KEY填写正确，res就是音频流了
#如果填写错误res就会使字典
print(res)

#接下来就把 res写进文件
with open("叮咚打开热水器1.mp3","wb") as f:
    f.write(res)

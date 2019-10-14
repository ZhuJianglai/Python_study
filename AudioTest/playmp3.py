# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 16:33
# @Author  : 081191
# @FileName: playmp3.py
# @Software: PyCharm

# playmp3.py 文件内容
import os



def play_mp3(file_name):
    #set SDL_AUDIODRIVER=directsound &&
    os.system("ffplay -autoexit -showmode 1 %s"%(file_name))

#play_mp3("hello.mp3")
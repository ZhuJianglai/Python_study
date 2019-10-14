# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 11:00
# @Author  : 081191
# @FileName: pyrec.py
# @Software: PyCharm
# pyrec.py 文件内容
import pyaudio
import wave
import os
import readconfig


# 定义数据流块
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
# RECORD_SECONDS = 10    #录制时长

def rec(file_name,RECORD_SECONDS):
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音,请说话......")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音结束,请闭嘴!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
#
# prodic = os.path.join(readconfig.prodir, "result", "rec")
# rec_name = prodic + "/190627.wav"
# print(rec_name)
#
# rec(rec_name)
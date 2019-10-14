# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 14:17
# @Author  : 081191
# @FileName: baidu_ai.py
# @Software: PyCharm
# baidu_ai.py 文件内容
from aip import AipSpeech

# 这里的三个参数,对应在百度语音创建的应用中的三个参数
APP_ID = "16550173"
API_KEY = "HBqG3EfrQKZNIz94GC9TO3IX"
SECRET_KEY = "tIo94eUp2lklaGRYR9FLedVCSIIGEdBt"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def audio_to_text(pcm_file):
    try:
        # 读取文件 , 终于得到了PCM文件
        with open(pcm_file, 'rb') as fp:
            file_context = fp.read()

        # 识别本地文件
        res = client.asr(file_context, 'pcm', 16000, {
            'dev_pid': 1536,
        })

        # 从字典里面获取"result"的value 列表中第1个元素,就是识别出来的字符串"老男孩教育"
        res_str = res.get("result")[0]

        return res_str
    except:
        res_str = "内容识别不出！！"
        return res_str
        print("内容识别不出！！")


def text_to_audio(res_str):
    synth_file = "synth.mp3"
    synth_context = client.synthesis(res_str, "zh", 1, {
        "vol": 5,
        "spd": 4,
        "pit": 9,
        "per": 4
    })

    with open(synth_file, "wb") as f:
        f.write(synth_context)

    return synth_file
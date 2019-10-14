# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 14:35
# @Author  : 081191
# @FileName: Runaudio.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import baidu_ai, pyrec
import playmp3  # 播放mp3 函数 文件
import wav2pcm  # wav转换pcm 函数文件



if __name__=='__main__':
    pyrec.rec("2.wav")  # 录音并生成wav文件,使用方式传入文件名

    pcm_file = wav2pcm.wav_to_pcm("2.wav")  # 将wav文件 转换成pcm文件 返回 pcm的文件名

    res_str = baidu_ai.audio_to_text(pcm_file) # 将转换后的pcm音频文件识别成 文字 res_str

    print(res_str)

    synth_file = baidu_ai.text_to_audio(res_str) # 将res_str 字符串 合成语音 返回文件名 synth_file

    playmp3.play_mp3(synth_file) # 播放 synth_file
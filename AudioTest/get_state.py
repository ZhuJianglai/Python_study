# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 13:43
# @Author  : 081191
# @FileName: get_state.py
# @Software: PyCharm
import requests
import json


_BASE_URL = 'https://rubyapi.vanward.com'
_API_URL = "/api/autotest/getDeviceStatus"
_HEADERS = {"Content-Type" : "application/x-www-form-urlencoded"}



def get_state():
    deviceId = 'c87dc4480bd84e9b9b0fbc8d60eef698'
    sign = 'ko2434asdjerberb4532423'
    response = requests.post(_BASE_URL+_API_URL, params= {'deviceId':deviceId,'sign':sign},headers = _HEADERS)
    r_stata = json.loads(response.content.decode())
    device_state = r_stata["IsOnline"]
    device_state1 = str(r_stata['Status']).replace('[','').replace(']','')
    fault_code = device_state1.split(',')[0]
    equip_onoff = device_state1[1]
    equip_mode = device_state1[2]
    equip_temp = device_state1[6]
    equip_state = device_state1[8]
    equip_zerocold = device_state1[18]
    try:
        equip_mode_info ={"是否在线":device_state, "故障":fault_code,"开关机":equip_onoff, '设备模式':equip_mode, "设置温度": equip_temp,"运行状态":equip_state, "零冷水":equip_zerocold}
        print(r_stata)
        print(equip_mode_info)
        return equip_mode_info
    except json.decoder.JSONDecodeError as e:
        print(e.msg)
        equip_mode_info = e.msg
        return equip_mode_info



if __name__ == '__main__':
    get_state()
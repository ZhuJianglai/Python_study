
import sys
import requests
import os
from socket import *
import ssl
import struct
import time, threading
import json
import base64
import hashlib

import configparser
TEST_WIFI_PID = "c9dde59a97"
TEST_WIFI_FID = "001GSWH002"
VERSION = '2.0.9'
heart = struct.pack('5B', int('10', 10), int('0', 16), int('0', 16), int('0', 16),int('0', 16))#心跳
MACSCENE = ['33:22:33:44:55:66',
            '33:22:33:44:55:99',
            '33:22:33:44:55:AA',
            '33:22:33:44:55:BB',
            '33:22:33:44:55:CC',
            '33:22:33:44:55:DD']
alldevice = dict()
http_post = 'https://api.westinghousewisdom.com/'
POSTHEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
_postdata = {}




import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def api_user_activeDevice(_MAC,_FID,_SSID,_SIGN,_VERSION):#wifi配网接口
    postdata_activeDevice = '{"Mac":"%s",' \
                              '"FirmwareId":"%s",' \
                              '"SSID":"%s",' \
                              '"Sign":"%s",' \
                              '"Fversion":"%s"}' % (_MAC, _FID, _SSID, _SIGN,_VERSION)
    # print(postdata_activeDevice)
    # imei+ "ruby" + fid + "vanward" + rand
    r = requests.post(http_post + "api/device/activeDevice", data=postdata_activeDevice)
    # noinspection PyBroadException
    try:
        resJson = json.loads(r.content.decode())
        # print(type(resJson))
        return str(r),resJson
    except:
        return str(r)


def SSID_toBASE64(_SSID):
    _SSID_BASE64 = base64.b64encode(_SSID.encode('utf-8'))
    return str(_SSID_BASE64,'utf-8')

def api_getimagecode():#获取图形验证码
    postsign = {"sign": "we2434asdjerberb324322#qw23fdqawe1232"}
    r = requests.post(http_post+"api/autotest/getImageCode", params=postsign, headers=POSTHEADERS)
    return r.content.decode().replace('"','')

def api_user_login_code(phonenumber,user_password,code):#app正常接口登录

    _postdata['mobile']=phonenumber
    _postdata['password'] = user_password
    _postdata['code'] = code
    #print(http_post)
    r = requests.post(http_post+"api/user/login", params=_postdata, headers=POSTHEADERS)
    resJson = json.loads(r.content.decode())
    #print(resJson)
    return str(r),resJson

def get_md5(IMEVALUE,MD5FID,RANDOMVALUE):
    stc = IMEVALUE + 'west'+MD5FID+'house' + RANDOMVALUE
    m = hashlib.md5()
    m.update(stc.encode("utf8"))
    psw = m.hexdigest()
    return psw

class app_Match:
    def __init__(self,_cellphone,_password):
        self.jsonRes = api_user_login_code(_cellphone, _password, api_getimagecode())
        self.uuid = self.jsonRes[1]['User']['Uuid']
        self.uutoken = self.jsonRes[1]['User']['Token']

class deviceidMatch:  # 定义父类
    def __init__(self,_uuid,_uutoken,_PID,_FID, _SSID,_MAC):

        self._post_data = dict()
        #self.jsonRes = api_user_login_code(_cellphone, _password, api_getimagecode())
        self.uuid = _uuid
        self.uutoken = _uutoken
        self.pid = _PID
        self.fid = _FID
        self.ssid = _SSID
        self.mac = _MAC
        self.baseSSID = SSID_toBASE64(self.ssid)
        self._post_data['uuid'] = self.uuid
        self._post_data['token'] = self.uutoken
        self._post_data['pid'] = self.pid
        self._post_data['firmwareId'] = self.fid
        self._post_data['ssid'] = self.baseSSID
        # print(self._post_data)
        requests.post(http_post + "api/user/bindInfo", params=self._post_data, headers=POSTHEADERS)
        self.md5 = get_md5(self.mac,self.fid, self.baseSSID)
        self.deviceJson = api_user_activeDevice(self.mac, self.fid, self.baseSSID, self.md5, VERSION)
        # print(self.deviceJson)
        self.deviceID = dict()
        self.deviceID['id'] = self.deviceJson[1]['DeviceId']
        self.deviceID['type'] = 1
        self.deviceToken = self.deviceJson[1]['Token']
        # print("uuid = %s" % self.uuid)
        # print("uutoken = %s" % self.uutoken)
        # print("deviceID = %s" % self.deviceID)
        # print("deviceToken = %s" % self.deviceToken)

        self.serverIP = gethostbyname("".join(self.deviceJson[1]['Domain']))  # 解析成IP地址
        # print(self.serverIP)

        self.socket = connect_socket_login(self.serverIP, self.deviceID, self.deviceToken)
        self.Recthread = threading.Thread(target=socket_recv, args=(self.socket,),
                                             name='deviceA_Thread')
        self.Recthread.start()

    def delete_thread(self):
        print("delete_thread")
        # stop_thread(self.Recthread)
        del self

    def __del__(self):
        print("__del__")
        # main_init()

def connect_socket_login(_serverIP,_deviceID,_deviceToken):
    _Socket = ssl.wrap_socket(socket(AF_INET, SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23)  # socket ssl
    # _loginheadstr = '{"Id":"%s","Token":"%s","Status":[24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}' % (_deviceID['id'], _deviceToken)
    _loginheadstr = '{"Id":"%s","Token":"%s","Status":[24,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]}' % (_deviceID['id'], _deviceToken)
    _loginheadlen = "%s" % (hex(len(_loginheadstr)))
    _loginhead = struct.pack('5B', int('0', 16), int('0', 16), int('0', 16), int('0', 16), int(_loginheadlen, 16))
    #print(_loginhead + _loginheadstr.encode())
    _Socket.connect((_serverIP, 2300))
    _Socket.sendall(_loginhead + _loginheadstr.encode())

    print("OP:[0,0,0,0,%d]"% (len(_loginheadstr)))
    print(_loginheadstr.encode())
    return _Socket

flat_heart_start=0
def Heart_beat_send(_Socket):
    global flat_heart_start,faild_time
    heat_beat = threading.Timer(120, Heart_beat_send, (_Socket,))  # 60秒调用一次函数
    heat_beat.start()  # 启用定时器

    if flat_heart_start==1:
        print("HeartBeat time is arrived")
        _Socket.sendall(heart)
    elif flat_heart_start==2:
        print("HeartBeat time is overtime")
        faild_time+=1
        restart_program()

    flat_heart_start += 1


def socket_recv(_Socket):
    global succsee_time,faild_time
    Heart_beat_send(_Socket)
    while True:
        # 每次最多接收1k字节:
        modifiedSentence = _Socket.recv(1024)
        if modifiedSentence:
            str_Recv = modifiedSentence.decode('utf-8')
            if len(str_Recv) >=5:
                print("OP:[%d,%d,%d,%d,%d]"%(modifiedSentence[0],modifiedSentence[1],modifiedSentence[2],modifiedSentence[3],modifiedSentence[4]))
                print(("Res[%d]:" + str_Recv)%(len(str_Recv)))
                if modifiedSentence[0]==10:
                    succsee_time +=1
                    print("Succsee")
                    restart_program()



def update_ini():
    global Test_Time,succsee_time,faild_time
    Test_Time = succsee_time + faild_time
    try:
        config.add_section("Mode")
    except configparser.DuplicateSectionError as a:
        config.set("Mode", "Sum", str(Test_Time))
        config.set("Mode", "Succsee", str(succsee_time))
        config.set("Mode", "Faild", str(faild_time))
        config.write(open('Cloud_Test.ini', "w"))

def restart_program():
    global Test_Time,succsee_time,faild_time
    update_ini()
    print("总次数:%d,成功:%d,失败:%d\r\n" % (Test_Time, succsee_time, faild_time))
    python = sys.executable
    os.execl(python, python, * sys.argv)



if __name__ == '__main__':
    Test_Time = 0
    succsee_time = 0
    faild_time = 0
    config = configparser.ConfigParser()
    try:
        config.read_file(open('Cloud_Test.ini'))
        str_Time = config.get("Mode","Sum")
        str_Succsee = config.get("Mode","Succsee")
        str_faild = config.get("Mode","Faild")
        # print(str_Time)
        # print(succsee_time)
        # print(str_faild)
        Test_Time = int(str_Time)
        succsee_time=int(str_Succsee)
        faild_time = int(str_faild)
    finally:
        app_a = app_Match("13810001020", "1234567a")
        deviceP = deviceidMatch(app_a.uuid, app_a.uutoken, TEST_WIFI_PID, TEST_WIFI_FID, "testsmart", MACSCENE[0])


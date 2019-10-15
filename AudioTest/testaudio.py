import doexcel
import os
import unittest
import paramunittest
import readconfig
from time import sleep
import psutil



test_xls= doexcel.get_xls("audioCase.xlsx", "dingdong_device_online")
localreadconfig = readconfig.ReadConfig()
prodir=readconfig.prodir
localpath=os.path.join(prodir, "wma/")
awaken = localpath+"awaken.mp3"
print(localpath)
print(awaken)


info = {}




@paramunittest.parametrized(*test_xls)
class Audio(unittest.TestCase):
    def setParameters(self, case_name, device_status, audio_name, audio_text, receive_voice_name, receive_voice_text, app_result, code, msg):
        """
        set params
        :param case_name:
        :param device_status:
        :param audio_name:
        :param audio_text:
        :param receive_voice_name:
        :param receive_voice_text:
        :param app_result:
        :param code:
        :param msg:
        :return:
        """

        self.case_name = str(case_name)
        self.device_status = str(device_status)
        self.audio_name = localpath + str(audio_name)
        self.audio_text = str(audio_text)
        self.receive_voice_name = str(receive_voice_name)
        self.receive_voice_text = str(receive_voice_text)
        self.app_result = str(app_result)
        self.code = str(code)
        self.msg = str(code)
        # self.return_json = None
        # self.info = None



    def discription(self):
        """
        test report description
        :return:
        """
        self.case_name



    def setUp(self):
        """

        :return:
        """
        print(self.case_name+"测试开始前准备")


    def testAudio(self):
        """
        test body
        :return:
        """
        #检测设备状态是在测试条件的状态

        #唤醒音响
        os.system("ffplay -autoexit -showmode 1 s%"(awaken))
        sleep(1)

        os.system("ffplay -autoexit -showmode 1 s%"(self.audio_name))





    def check_status(self,):



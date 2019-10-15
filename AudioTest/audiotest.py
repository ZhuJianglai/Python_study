import os
import readconfig
from time import sleep
from datetime import datetime
import doexcel
import pyrec
import wav2pcm
import baidu_ai



localreadconfig = readconfig.ReadConfig()
prodir=readconfig.prodir
localpath=os.path.join(prodir, "wma/")
# awaken = localpath+"awaken.wma"
awaken = os.path.join(prodir, "wma/", "awaken.wma")
# print(localpath)
# print(awaken)



# 创建测试输出excel
test_xls_name = "TestResult%s.xls"%(datetime.now().strftime("%y%m%d%H%M%S"))
test_xls_title = [["case_name", "device_status", "answer_rec", "answer_text", "audio_name", "receive_voice_name", "receive_voice_text", "app_result", "code", "msg"],]
resultPro = os.path.join(prodir, "result/", test_xls_name)
doexcel.create_new_xls(resultPro, "testResult", test_xls_title)

test_result = []


def testAudio(test_xls, awaken):
    """
    test body
    :return:
    """
    rec_path = os.path.join(prodir, "result", "rec")
    #检测设备状态是在测试条件的状态
    for i in range(0, len(test_xls)):

        audio_name = test_xls[i][2]
        case_name = test_xls[i][0]
        # print(audio_name)
        # print(case_name)
        # print(awaken)
         #唤醒音响
        os.system("ffplay -autoexit -showmode 1 %s"%(awaken))
        # sleep(1)
        answer_rec = rec_path + "/answer%s.wav"%(datetime.now().strftime("%y%m%d%H%M%S"))
        print(answer_rec)
        pyrec.rec(answer_rec,2)
        pcm_name_answer = wav2pcm.wav_to_pcm(answer_rec)
        answer_text = baidu_ai.audio_to_text(pcm_name_answer)
        os.system("ffplay -autoexit -showmode 1 %s"%(localpath+audio_name))
        # sleep(1)
        rec_name = rec_path + "/rec%s.wav"%(datetime.now().strftime("%y%m%d%H%M%S"))
        print(rec_name)
        pyrec.rec(rec_name,8)
        pcm_name = wav2pcm.wav_to_pcm(rec_name)
        rec_text = baidu_ai.audio_to_text(pcm_name)
        test_result = [case_name, "", answer_rec, answer_text, audio_name, rec_name, rec_text]
        print(test_result)
        doexcel.write_xls_app(resultPro, test_result)



test_xls= doexcel.get_xls("audioCase.xlsx", "dingdong_device_online")
testAudio(test_xls, awaken)







import logging
from datetime import datetime
import threading
import readConfig
import os


class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # create result file if it doesn't exist

        if not os.path.exists(resultPath):
            os.mkdir(resultPath)

        #defind test result file name by localtime

        logPath=os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%S")))

        #create test result file if it doen't exist

        if not os.path.exists(logPath):
            os.mkdir(logPath)


        #定义logger
        self.logger=logging.getLogger()

        #定义log的等级
        self.logger.setLevel(logging.INFO)

        #defined handler

        handler=logging.FileHandler(os.path.join(logPath,"output.log"))

        #defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #defind formatter
        handler.setFormatter(formatter)

        #defind handler
        self.logger.addHandler(handler)



class MyLog:
    log=None
    mutex = threading.Lock()

    def __ini__(self):

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log=Log()
            MyLog.mutex.release()

        return MyLog.log


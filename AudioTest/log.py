import os
import readconfig
from datetime import  datetime
import logging
import threading



class result_xls:
    def __init__(self):
        global resultPath, proDir, logPath
        proDir = readconfig.prodir
        resultPath = os.path.join(proDir, "result")
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        #定义headler
        handler = logging.FileHandler(os.path.join(logPath, "out.log"))

        #定义格式
        formatter = logging.FileHandler('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)


    def get_logger(self):
        """
        get logger
        :return:
        """

        return self.logger


    def build_start_line(self,case_no):
        """
        打印开始测试
        :param case_name:
        :return:
        """
        self.logger.info("----------" + case_no + "Start -------------------")

    def build_end_line(self,case_no):
        """
        打印结束
        :param case_name:

        :return:
        """
        self.logger.info(("----------" + case_no + "End -------------------"))

    def build_case_line(self,case_name, code,msg):
        """
        write test case line
        :param case_name:
        :param code:
        :param msg:
        :return:
        """

    def get_report_path(self):
        """
        get report path
        :return:
        """
        report_path = os.path.join(logPath,"report.html")
        return  report_path

    def get_result_path(self):
        """
        get test result path
        :return:
        """
        return logPath

    def write_result(self, result):
        """

        :param result:
        :return:
        """
        result_path = os.path.join(logPath, "report.txt")
        fb = open(result_path, "wb")
        try:
            fb.write(result)
        except FileNotFoundError as ex:
            logger.error(str(ex))


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    logger.info("test info")

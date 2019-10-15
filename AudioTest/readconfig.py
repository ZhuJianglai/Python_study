import os
import codecs
import configparser

prodir = os.path.split(os.path.realpath(__file__))[0]
configpath = os.path.join(prodir, "config.ini")
# print(configpath)


class ReadConfig:
    def __init__(self):
        fd = open(configpath)
        data = fd.read()

        #remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data=data[3:]
            file = codecs.open(configpath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_mail(self , name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self,name):
        value = self.cf.get("HTTP", name)
        return value

    def get_baiduaip(self,name):
        value =self.cf.get("BAIDUAIP", name)
        return value

    def get_header(self,name):
        value =self.cf.get("HRADERS", name)
        return value



# print(ReadConfig().get_http("scheme"))
# print(ReadConfig().get_baiduaip("APP_ID"))
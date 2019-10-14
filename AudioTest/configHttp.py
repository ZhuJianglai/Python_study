# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 11:40
# @Author  : 081191
# @FileName: configHttp.py
# @Software: PyCharm
from AudioTest import readconfig

localReadConfig = readconfig.ReadConfig()

class ConfigHttp:

    def __int__(self):
        global scheme, baseurl, port, timeout
        scheme=localReadConfig.get_http("scheme")
        baseurl=localReadConfig.get_http("baseurl")
        port=localReadConfig.get_http("port")
        timeout=localReadConfig.get_http("timeout")



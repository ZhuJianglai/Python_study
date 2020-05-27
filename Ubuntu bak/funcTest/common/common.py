import os
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from common.Log import MyLog as Log
import readConfig
from common import configHttp




localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

#从excel中读取用例
def get_exxcel(xls_name,sheet_name):
    global proDir
    proDir=readConfig.proDir
    cls=[]
    #get xls's path
    xlspath=os.path.join(proDir, "testfile", xls_name)
    file=open_workbook(xlspath)

    #get sheet by name
    sheet=file.sheet_by_name(sheet_name)

    #get one sheet's rows
    nrow=sheet.nrows
    for i in range(nrow):
        if sheet.row_values(i)[0]!=u'case_name':
            cls.append(sheet.row_values(i))
    return cls





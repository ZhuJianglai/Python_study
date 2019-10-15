import xlrd
import os
import readconfig as readconfig
from  xlutils.copy import copy
import xlwt

localreadconfig=readconfig.ReadConfig()
prodir=readconfig.prodir

# print(prodir)



caseNo=0




def get_xls(xls_name,sheet_name):
    '''

    get date from xls file
    :param xls_name:
    :param sheet_name:
    :return:
    '''
    cls = []

    #get xls file's path
    xlsPath = os.path.join(prodir, xls_name)
    # print(xlsPath)
    #open xls file
    file = xlrd.open_workbook(xlsPath)
    #get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    #get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] !=u'case_name':
            # print(sheet.row_values(i))
            cls.append(sheet.row_values(i))
    return cls

#
# print(get_xls("audioCase.xlsx", "login"))
# print(get_xls("audioCase.xlsx", "login")[0][0])
# print(len(get_xls("audioCase.xlsx", "login")))
# A=get_xls("audioCase.xlsx", "login")
# for i in range(0, len(A)):
#     for j in range(0,len(A[i])):
#             print(A[i][j])


def write_xls_app(path, value):
    index = len(value) #获取要写入数据的数
    workbook = xlrd.open_workbook(path) #打开工作薄
    sheets = workbook.sheet_names()#获取工作薄中所有的表格
    worksheet = workbook.sheet_by_name(sheets[0])# 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows #获取表格中已存在的数据行数
    new_workbook = copy(workbook) #将xlrd转换为xlwt对象
    new_worksheet = new_workbook.get_sheet(0) #获取转化后工作表
    for i in range(0, index):
        new_worksheet.write(rows_old, i, value[i])  # 追加写入数据，注意是从rows_old行开始写入
    new_workbook.save(path) #保存工作薄
    print("写入成功")


def write_xls_app_1(path,value):
    index = len(value) #获取要写入数据的行数
    workbook = xlrd.open_workbook(path) #打开工作薄
    sheets =workbook.sheet_names()#获取工作薄中所有的表格
    worksheet = workbook.sheet_by_name(sheets[0])# 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows #获取表格中已存在的数据行数
    new_workbook = copy(workbook) #将xlrd转换为xlwt对象
    new_worksheet = new_workbook.get_sheet(0) #获取转化后工作表
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old, j, value[i][j])
    new_workbook.save(path) #保存工作薄
    print(value+"写入成功")


def create_new_xls(path, sheet_name, value):
    index = len(value)
    workbook = xlwt.Workbook(path)
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    workbook.save(path)
    print("创建xls成功")
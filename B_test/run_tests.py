# -*- coding: utf-8 -*-
# @Time    : 2018-12-19 14:41
# @Author  : 081191
# @FileName: run_tests.py.py
# @Software: PyCharm

import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest


#指定测试用例为当前文件夹的interface目录

test_dir ='./interface'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename= './report/'+now +'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title="Tmall Api Test")
    runner.run(discover)
    fp.close()
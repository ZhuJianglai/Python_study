# -*- coding: utf-8 -*-
# @Time    : 2018-12-20 12:00
# @Author  : 081191
# @FileName: add_test.py
# @Software: PyCharm

import os
import test
import unittest


class AddTest(unittest.TestCase):

    def setUp(self):
        print("开始测试")
    def tearDown(self):
        print("结束测试")

    def test_add(self):
        self.c=test.add(2,5)
        print(self.c)
        self.assertEqual(self.c, 7)
        print("ok")


if __name__ =="__main__":
    unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(AddTest('add_test'))
    runner =unittest.TextTestRunner()
    runner.run(suite)
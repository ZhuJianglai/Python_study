# -*- coding: utf-8 -*-
# @Time    : 2018-12-19 11:55
# @Author  : 081191
# @FileName: tmallbund_test.py
# @Software: PyCharm

import requests
import unittest

_HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}

class BundTmallTest(unittest.TestCase):

    def setUp(self):
        print("test start")
        self.url='https://rubyapi.vanward.com/auth/login'

    def test_bund_moblie_null(self):
        r=requests.post(self.url,params={'mobile':'','password':'1234567a'},headers= _HEADERS)
        # print(r)
        result=r.json()
        # print(result)
        self.assertEqual(r.status_code,401)
        self.assertIsNotNone(result)
        self.assertEqual(result,'登录失败,账号或密码错误')


    def test_bund_password_Error(self):
        r=requests.post(self.url,params={'mobile':'13810001005','password':'1234567'},headers= _HEADERS)
        # print(r)
        result=r.json()
        # print(result)
        self.assertEqual(r.status_code,401)
        self.assertIsNotNone(result)
        self.assertEqual(result,'登录失败,账号或密码错误')


    def test_bund_succes(self):
        r=requests.post(self.url,params={'mobile':'13810001005','password':'1234567a'},headers= _HEADERS)
        # print(r)
        result=r.json()
        # print(result)
        self.assertEqual(r.status_code,200)
        self.assertIsNotNone(result)
        print(result)

    def tearDown(self):
        print("test end")

if __name__ =='__main__':
    unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(BundTmallApiTest('test_bund_moblie_null'))
    # suite.addTest(BundTmallApiTest('test_bund_password_Error'))
    # suite.addTest(BundTmallApiTest('test_bund_succes'))
    # runner =unittest.TextTestRunner()
    # runner.run(suite)
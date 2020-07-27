# -*- coding: utf-8 -*-
# @Time    : 2020-7-27 0027 18:42 
# @Author  : 081191 
# @FileName: test.py                     
# @Software: PyCharm 
# !/usr/bin/python
from django.test import TestCase

from apitest.views import test,home,login
from django.urls import reverse
from django.http import HttpRequest

class titlePageTest(TestCase):
    def test_loginpage_returns_title_html(self):
        request=HttpRequest()
        response=login(request)
        self.assertIn(b'<title>AutotestPlat</title>',response.content)




class contentTest(TestCase):
    def test_content_url_resolves_to_view(self):
        request=HttpRequest()
        response=login(request)
        self.assertIn(b'test123456',response.content)
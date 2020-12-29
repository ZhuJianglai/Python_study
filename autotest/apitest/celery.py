# -*- coding: utf-8 -*-
# @Time    : 2020-8-20 23:31  
# @Author  : Administrator
# @FileName: celery.py
# @Software: PyCharm
# !/usr/bin/python


from __future__ import absolute_import
import os
import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','autotest.settings')
django.setup()

app=Celery('autotest')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda:settings.INSRALLED_APPS)
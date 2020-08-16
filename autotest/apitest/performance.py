# -*- coding: utf-8 -*-
# @Time    : 2020-8-15 22:23  
# @Author  : Administrator
# @FileName: performance.py.py
# @Software: PyCharm
# !/usr/bin/python

from locust import HttpUser,task,between

class WebsiteTasks(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    wait_time = between(5,15)

#locust 1.1.1已不适用，使用wait_time
# class websiteUser(HttpUser):
#     task_set=WebsiteTasks
#     min_wait=100
#     max_wait=1000

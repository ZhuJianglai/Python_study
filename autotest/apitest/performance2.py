# -*- coding: utf-8 -*-
# @Time    : 2020-8-15 22:32  
# @Author  : Administrator
# @FileName: performance2.py
# @Software: PyCharm
# !/usr/bin/python


from locust import HttpUser,task,between

class WebsiteTasks(HttpUser):
    @task
    def login(self):
        self.client.post("/login/",{
            "username":"admin",
            "password":"1234567a"
        })
    wait_time = between(5,30)

# #locust 1.1.1已不适用，使用wait_time
# class WebsiteUser(HttpUser):
#     task_set=WebsiteTasks
#     min_wait=100
#     max_wait=1000

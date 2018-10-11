# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

import time
user,passwd='alex','abc123'
def auth(func):
    def wrapper(*args,**kwargs):
        username=input("Username").strip()
        password=input("Password").strip()
        if user ==username and passwd==password:
            func
            dsad das


def index():
    print("welcome to index page")

def home():
    print("welcome to home page")

def bbs():
        print("welcome to bbs page")


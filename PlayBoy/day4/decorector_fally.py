# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-


user,passwd='alex','abc123'
def auth(func):
    def wrapper(*args,**kwargs):
        username=input("Username:").strip()
        password=input("Password:").strip()
        if user ==username and passwd==password:
          print("\33[32;1mUser has passed authentiacation\033[0m")
          res=func(*args,**kwargs)
          print("---after authentication")
          return res
        else:
          exit("\33[32;1mInvalid username or password\033[0m")
    return wrapper


def index():
    print("welcome to index page")

@auth
def home():
    print("welcome to home page")
    return "from home"
@auth
def bbs():
        print("welcome to bbs page")

index()
print(home())
bbs()


# author：zhu
#!/usr/bin/env python
# -*-coding:utf-8 -*-

## day4 第9课
user,passwd='alex','abc123'
# def auth(func):
#     def wrapper(*args,**kwargs):
#         username=input("Username:").strip()
#         password=input("Password:").strip()
#         if user ==username and passwd==password:
#           print("\33[32;1mUser has passed authentiacation\033[0m")
#           res=func(*args,**kwargs)
#           print("---after authentication")
#           return res
#         else:
#           exit("\33[32;1mInvalid username or password\033[0m")
#     return wrapper
#添加参数后
user,passwd='alex','abc123'
def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type=="local":
                username=input("Username:").strip()
                password=input("Password:").strip()
                if user ==username and passwd==password:
                  print("\33[32;1mUser has passed authentiacation\033[0m")
                  res=func(*args,**kwargs)
                  print("---after authentication")
                  return res
                else:
                  exit("\33[32;1mInvalid username or password\033[0m")
            elif auth_type=="ldap":
                print("搞毛线，不会了。。。。")
        return wrapper
    return out_wrapper

#测试pull
def index():
    print("welcome to index page")

@auth(auth_type="local") #添加参数
# @auth
def home():
    print("welcome to home page")
    return "from home"

# @auth
@auth(auth_type="ldap") #添加参数
def bbs():
        print("welcome to bbs page")

index()
print(home())
bbs()


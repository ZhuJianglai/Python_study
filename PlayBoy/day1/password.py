import getpass
#if ...else ..判断
_username="zhu"
_password="1234"
username=input("usename:")
# password=getpass.getpass("password:")
password=input("password:")
# print(usename,password)


if _username==username and _password ==password:
    print("welcome user {name} login ...".format(name=username))
else:
    print("Invalid username or passwold!")
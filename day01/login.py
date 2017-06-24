#Author:ithuplion
_username = "ithuplion"
_password = "123"
loginname = input("loginname:")
password = input("password:")
if loginname == _username and password == _password:
    print("Welcome user {name} login".format(name=loginname))
else:
    print("Invalid username or password")
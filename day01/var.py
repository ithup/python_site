#Author:ithuplion
username = input("username:")
password = input("password：")
age = input("age:")
sex = input("sex:")
info = '''
-------------inofs------------------
username:{0}
passwrod:{1}
age:{2}
sex:{3}
'''.format(username,password,age,sex)
print(info)
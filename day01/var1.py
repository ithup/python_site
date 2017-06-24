#Author:ithuplion
username = input("username:")
password = input("password：")
age = input("age:")
sex = input("sex:")
info = '''
-------------inofs------------------
username:{_name}
passwrod:{_pwd}
age:{_age}
sex:{_sex}
'''.format(_name=username,_pwd=password,_age=age,_sex=sex)
print(info)

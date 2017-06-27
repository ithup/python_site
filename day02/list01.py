#Author:ithuplion
names = ["tom","rose","jack","zhangsan"]
print("-----------遍历元素---------------")
print(names)
for i in range(4):
    print(names[i])
print("--------------切片----------------------")
print(names[1:2])   #切片
print(names[-1])   #取最后一个元素
print(names[-2:-1])
print(names[-2:])
print(names[0:4])
print(names[:4])
print("---------------添加元素-----------------------------")
names.append("郭靖")
print(names)
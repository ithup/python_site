#Author:ithuplion
names = ["tom","rose","12jack","Zhangsan","rose","#*jack","zhangsan","rose"]
print("-----------遍历元素---------------")
print(names)
# for i in range(4):
#     print(names[i])
print("--------------切片----------------------")
print(names[1:2])   #切片
print(names[-1])   #取最后一个元素
print(names[-2:-1])
print(names[-2:])
print(names[0:4])
print(names[:4])
print("---------------添加元素-----------------------------")
# names.append("郭靖")
# names.insert(1,"周三")
# names.insert(3,"王五")
# print(names)
print("--------------删除元素--------------")
# names.remove("rose")
# names.pop()
# del names[2]
print(names)
print("----------------修改元素-----------------")
# names[2] = "娜娜"
# print(names)
print("-----------获取元素下标索引,查询------------------")
# name_index = names.index("jack")
# name=names[name_index]
# print(name_index,name)
print(names.count("rose"))
print("----------------清空列表，反转，排序，扩展、合并-----------------------------")
# names.clear()
# print(names)
# names.reverse()
# print(names)
#特殊符号>数字>大写字母>小写字母
# names.sort()
# print(names)
names2 = [1,2,3,4,5]
names.extend(names2)
print(names,names2)
#删除列表变量
del names2
# print(names2)
print(names)
print("----------循环-----------")
for i in names:
    print(i)
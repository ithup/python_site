#Author:ithuplion
myage=input("my age:")

count = 0;
while count<3:
    user_input = input("input your guess number:")
    if user_input == myage:
        print("Congratulations,you get it")
    elif user_input>myage:
        print("bigger")
    else:
        print("smaller")
    count+=1
else:
    print("很遗憾你次数已用完")
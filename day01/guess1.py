#Author:ithuplion
ithuplion = 22
count = 0
while True:
    if count==3:
         print("你猜的次数已过")
         break
    guess_age = int(input("guess_age:"))
    if guess_age == ithuplion:
        print("yes,you get it.")
        break
    elif guess_age > ithuplion:
         print("guess bigger")
    else:
         print("guess smaller")
    count+=1

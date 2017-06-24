#Author:ithuplion
ithuplion = 22
count = 0
while count<3:
    guess_age = int(input("guess_age:"))
    if guess_age == ithuplion:
        print("yes,you get it.")
        break
    elif guess_age > ithuplion:
         print("guess bigger")
    else:
         print("guess smaller")
    count+=1
else:
    print("you hava tried too many times ..")
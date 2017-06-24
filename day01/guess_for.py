#Author:ithuplion
ithuplion = 22
for i in range(3):
    guess_age = int(input("guess_age:"))
    if guess_age == ithuplion:
        print("yes,you get it.")
        break
    elif guess_age > ithuplion:
         print("guess bigger")
    else:
         print("guess smaller")
else:
    print("you hava tried too many times ..")
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
    if count == 3:
        continue_confirm = input("do you want to keep guessing ...?y/n")
        if continue_confirm == "y":
            count=0
        elif continue_confirm == "n":
            print("欢迎下次再来................")
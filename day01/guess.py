#Author:ithuplion
ithuplion_age = 22
guess_age = int(input("guess age:"))
if guess_age == ithuplion_age:
    print("yes,you get it.")
elif guess_age>ithuplion_age:
    print("guess bigger")
else:
    print("guess smaller")
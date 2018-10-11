#zhu


import random
count = 0
age_of_oldboy = random.randint(18,80)
while count<3:
    guess_age=int(input("please input age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif guess_age>age_of_oldboy:
        print("think bigger..")
    else:
        print(("think smaller.."))
    count = count + 1
else:
    print("you hava tried many time..fuck off")
    print(age_of_oldboy)
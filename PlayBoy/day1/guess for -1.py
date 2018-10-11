#zhu


import random
count = 0
age_of_oldboy = random.randint(18,80)
for i in range(1,3):
    guess_age=int(input("please input age:"))
    if guess_age == age_of_oldboy:
        print("yes,you got it.")
        break
    elif guess_age>age_of_oldboy:
        print("think bigger..")
    else:
        print(("think smaller.."))
    print(age_of_oldboy)
    if count == 3:
        comform =input("00000.")
        if comform == 0:
            count = 0
# else:
#     print("you hava tried many time..fuck off")

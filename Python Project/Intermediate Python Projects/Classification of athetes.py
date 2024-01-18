from datetime import date
atual = date.today().year
year_of_birth = int(input("Your Year of birth:"))
age = atual - year_of_birth

if age <=9:
    print("You are {} years old, you are on the Foundation section".format(age))
elif age <=14:
    print("You are {} years old, you are in the Children section ".format(age))
elif age<= 19:
    print("You are {} Years old, you are on the Junior section".format(age))
elif age <= 25:
    print("You are {} years old, you belong to the Senior section ".format(age))
else:

    print("You are a Master you have {} years old".format(age))
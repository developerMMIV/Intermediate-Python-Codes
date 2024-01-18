from datetime import date
atual = date.today().year
Y_O_B = int(input("Your year of birth:"))
age = atual - Y_O_B

if age ==18:
    print("You are {} , Go for your enlistment now".format(age))
elif age >= 18:
    adultage = age - 18
    print("You are {}, You would have done your enlistment in the year {}".format(age,atual-adultage))
else:
    upcomingage =  18- age
    print("You are {}, You will do your entitilment in {}  ".format(age, atual+upcomingage))

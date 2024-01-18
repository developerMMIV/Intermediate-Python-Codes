name = input("What is your name?:")

print("Welcome to the wife material test, created by @developergustavoMMIV this is a test if you are worthy to be an wife material")
print("{} in order to pass ths test, you must get at least 70% (C) if you really a wife material or not ".format(name))
input("You must type yes or no, else the system won't recognise your answer and the complete points given by you. Press any key to start")
point = 0

question1 = int(input("1: How old are you?"))
if question1  <= 29:
    point += 10

question2 = input("2 :Are you a virgin? ").lower()
if question2 == "yes":
    point += 10
elif question2 == "no":
     body = int(input("How many body counts do you have?:"))
     if body == 1<= 5:
         point += 8
     elif body == 5 <= 7:
         point += 6
     elif body == 8 <= 10:
         point += 4
     elif body >= 10:
         point += 0

question3 = input("3: Do you have a father figure?").lower()
if question3 == "yes":
    point +=10
elif question3== "no" :
    point +=6

question4 = input("4: Do you know how to cook?").lower()
if question4 == "yes":
    point += 10

question5 = input("5: Do you insult, become agressive, and retalilate if someone annoys you?").lower()
if question5 == "yes":
    point += 2
elif question5== "Sometimes" and "Maybe":
    point+= 5.5
elif question5 == "no":
     point+= 10

question6 = input("6: Do you go to girls trips? (even if it is going to the clubs, or places that are not approving to the public with your female friends) ").lower()
if question6 == "yes":
     point+=4
elif question6 == "no":
    point += 10

question7 = input("7:Were you once in a relationship").lower()
if question7 == "yes":
     why = input("Were you the one that ended the relationship?").lower()
     if why =="yes":
        point+= 2
     elif why == "no":
        point += 6
elif question7== "no":
    point+=10

question8 = input("8: Are your friends promiscuous?").lower()
if question8 == "yes":
    point+=4
elif question8 == "no":
    point+=10


question9 = input("9:Do you prefer (a) a man that is above 6ft, net worth from $500,000 and handsome or (b) a man that loves you. press A or B ").lower()
if question9 == "a":
    point+=0
elif question9 =="b":
    point+=10


question10 = input("10:Two questions to answer yes and no, if your partner cheats on you, are you breaking up "
                   "and does your happiness in the relationship matter? type your answer without any symbol ").lower()
if question10 == "yes yes":
    point+= 2.5
elif question10== "yes no":
    point+= 5.0
elif question10=="no yes":
    point+= 7.5
elif question10== "no no":
    point+= 10


print("Fetching Results..........")
print("="*20)
print("="*20)



if point<40:
    print("{}, unfortunately, you are not capable to become a wife material, you are a feminist, your score is {} and that is a F ".format(name, point))
elif point<=50:
    print("{}, unfortunately, you are not capable to become a wife material, you will divorce your partner and collect all of his belongings in the future,"
          " your score is {} and that is an E".format(name,point))
elif point<=60:
    print("{}, unfortunately, you are not capable to become a wife material, you are very promiscuous or you love atrtactive men that covers 1% of the world population,"
          " your score is {} and that is a D".format(name,point))
elif point<=70:
    print("{}, you are a wife material, but you are only atracted to High Value Men. Your score is {} and that is a C ".format(name,point))
elif point<=80:
    print("{}, you are a wife material, but try to work on yourself before dating (just an advice). Your score is {} and that is a B".format(name,point))
elif point >=90:
    print("{}, YOU ARE A WIFE MATERIAL!!! You belong in the 20% of the world population. Your score is {} and that is an A".format(name, point))








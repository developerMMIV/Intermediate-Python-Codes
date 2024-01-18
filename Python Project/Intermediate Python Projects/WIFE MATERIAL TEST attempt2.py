from time import sleep
nome = input("What is your name?:").capitalize()

print("Loading Test................."
      "...........................")
sleep(3)

print('''Welcome to the Wife Material Test (WMT) version 1.2  created by @developergustavoMMIV.
 This is to test if YOU are worthy you be called a wife material ''')
print('''
''')

print('''{} if you want to pass this test, you must have to pass the average of 70% (C)
 if you want to be called a wife material. The general cut-off is 50% '''.format(nome))

input("You have to choose each number given to you else it will be invalid. Press Any Key to start  ")
sleep(2)
point = 0


question1 = int(input('''Question 1: How old are you?:
[ 1 ] 18 - 25
[ 2 ] 26 - 29
[ 3 ] 30 + 
 Answer: '''))
while question1 != 3 and question1 !=2 and question1 !=1:
      question1= int(input("Invalid Answer, Try again:"))

if question1 ==1:
      point+=10
elif question1 ==2:
      point+=9
elif question1 ==3:
      point+=0
else:
      print("Invalid answer, - 1pt")

question2 = int(input('''Question 2: Do you love/respect your father :
[ 1 ] Yes
[ 2 ] No
[ 3 ] Yes but he died
 Answer: '''))
while question2 != 3 and question2 !=2 and question2 !=1:
      question2= int(input("Invalid Answer, Try again:"))

if question2 ==1:
      point+=10
elif question2 ==2:
      point+=0
elif question2==3:
      point+=9.9
else:
      print("Invalid answer, try again")

question3 = int(input('''Question 3: What is your body count:
[ 1 ] Virgin
[ 2 ] 1 to 5
[ 3 ] 6 and above
Answer: '''))
while question3 != 3 and question3 !=2 and question3 !=1:
      question3= int(input("Invalid Answer, Try again:"))

if question3 ==1:
      point+= 10
elif question3 ==2:
      point+= 5
elif question3 ==3:
      point+= 1
else:
      print("Invalid answer, -1pt")

question4 = int(input('''Question 4 : Do you know how to cook?:
[ 1 ] Yes
[ 2 ] No
[ 3 ] Maybe...
Answer: '''))
while question4 != 3 and question4 !=2 and question4 !=1:
      question4= int(input("Invalid Answer, Try again:"))

if question4 == 1:
      point+= 10
elif question4 ==2:
      point+= 5
elif question4 ==3:
      point+= 0
else:
      print("Invalid answer, -1pt")

question5= int(input('''Question 5: Do you abuse,insult, become aggressive and retalilate if someones annoys you?
[ 1 ] Yes
[ 2 ] No
[ 3 ] Sometimes....
Answer: '''))
while question5 != 3 and question5 !=2 and question5 !=1:
      question5= int(input("Invalid Answer, Try again:"))

if question5 == 1:
      point+=0
elif question5 ==2:
      point+=10
elif question5 == 3:
      point+=2
else:
      print('Invalid answer, -1pt')

question6= int(input('''Question 6: Do you go to any trips, clubs, or places that is not appropriate for one to go alone and/or with your friends? 
[ 1 ] Yes
[ 2 ] No
[ 3 ] I used to/Once/it is complicated
Answer: '''))
while question6 != 3 and question6 !=2 and question6 !=1:
      question6= int(input("Invalid Answer, Try again:"))

if question6==1:
      point+=0
elif question6 == 2:
      point+=10
elif question6==3:
      point+= 5
else:
      print('Invalid answer, -1pt')

question7 = int(input('''Question 7: Were you in a relationship?
[ 1 ] Yes, i broke up
[ 2 ] Yes, he broke up
[ 3 ] No
Answer: '''))
while question7 != 3 and question7 !=2 and question7 !=1:
      question7= int(input("Invalid Answer, Try again:"))

if question7==1:
      point+=2
elif question7==2:
      point+=4
elif question7==3:
      point+=10
else:
      print("Invalid answer, -1pt")

question8 = int(input('''Question 8: Are your friends I feminists/ II promiscuous
[ 1 ] I only
[ 2 ] II only
[ 3 ] All of the above
[ 4 ] None of the above
[ 5 ] I don't have friends
Answer: '''))
while question8 != 3 and question8 !=2 and question8 !=1 and question8 !=5 and question8!=4:
      question8= int(input("Invalid Answer, Try again:"))

if question8==1:
      point+=0
elif question8==2:
      point+=1
elif question8==3:
      point+=0
elif question8==4:
      point+= 10
elif question8==5:
      point+=10
else:
      print("Invalid answer, -1pt")

question9 = int(input(''' Question 9: Which type of man do you want?
[ 1 ] 6ft,net worth of $500k and above, handsome
[ 2 ] A man that loves you (Simp)
[ 3 ] Either of the options above
Answer: '''))
while question9 != 3 and question9 !=2 and question9 !=1:
      question9= int(input("Invalid Answer, Try again:"))

if question9==1:
      point+=0
elif question9 == 2:
      point+=10
elif question9==3:
      point+=5
else:
      print("Invalid answer, -1pt")

question10 = int(input('''Question 10: Two questions, if your partner cheats on you, are you gonna leave?
 And does your happiness/intrest in the relationship matters?
[ 1 ] Yes,Yes
[ 2 ] Yes, No
[ 3 ] No, Yes
[ 4 ] No, No
  Answer:  '''))
while question10 != 3 and question10 !=2 and question10 !=1 and question10 !=4:
      question10= int(input("Invalid Answer, Try again:"))

if question10 == 1:
      point+=2.5
elif question10==2:
      point+= 5
elif question10 == 3:
      point+= 7.5
elif question10 == 4:
      point+= 10
else:
      print("Invalid answer, -1pt")

print('Loading Results.................')

sleep(5)



if point<49:
      print("                                    {}%                                                 ".format(point))
      print('''{} You are not capable to become a wife material, your score is {} and that is a F.
       Stop being a feminist or else you will live with cats'''.format(nome,point))
elif point <59:
      print("                                    {}%                                              ".format(point))
      print('''{} you are not capable to become a wife material, your score is {} and that is an E.
      Please learn how to respect men and be learn how to be submissive as well as men were the ones that built this world that you're living now
      P.S. The Truth is bitter'''.format(nome,point))
elif point <69:
      print("                                    {}%                                           ".format(point))
      print('''{} you are not capable to be a wife material, your score is {} and that is a D.
      Please stop being more promiscuous as you are as it can ruin your partner's future 
      P.S The Truth is bitter'''.format(nome,point))
elif point <79:
      print("                                    {}%                                                ".format(point))
      print('''{} You are a wife material, your score is {} and that is a C.
      But try to understand that to find successsful men wants monogamy is very rare, they MUST cheat on you 
      P.S Truth can only save lives'''.format(nome,point))
elif point <89:
      print("                                    {}%                                                 ".format(point))
      print('''{} You are a wife material  your score is {} and that is a B.
      But work on yourself before getting a partner'''.format(nome,point))
elif point >= 90:
      print("                  WIFE              {}%          MATERIAL                                          ".format(point))
      print('''{} YOU ARE A WIFE MATERIAL!!!!  your score is {} and that is an A!!
      you belong of the 20% of the women that are conservative with their family, religion and social values in this world  '''.format(nome,point))


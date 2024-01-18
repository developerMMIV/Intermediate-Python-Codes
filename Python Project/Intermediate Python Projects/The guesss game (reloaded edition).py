from random import randint
computer = randint(0,20)
computer2 = randint(0,10)
computer3 =randint(0,30)
op = 0
print("Hey, welcome to the advanced version of the guess game")
print('''Chosse any number for your level of dificulty
[ 1 ] Easy
[ 2 ] Medium
[ 3 ] Hard''')
option = int(input(":"))
while option != 1 and option != 2 and option !=3:
    option= int(input("Try again:"))
if option == 1:
    op = computer
elif option == 2:
    op = computer2
elif option == 3:
    op = computer3

correct = False
attempts = 0

while not correct:
    player = int(input("What is your attempt? "))
    attempts+=1
    if player == op:
        correct= True
    else:
        if player < op:
            print("More, try again")
        elif player>op:
            print("Less, try again")
print('You have got the answer with {} attempts'.format(attempts))


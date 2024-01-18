#from random import randint
#from time import sleep
items = ('Paper','Rock', 'Scissors')
computer =  randint(0,2)
print('''Your Options:
[ 0 ] Paper
[ 1 ] Rock
[ 2 ] Scissors''')
jogador = int(input("What is your option? "))
print("Rock")
sleep(2)
print("Paper")
sleep(2)
print("Scissors")

print("-="*11)
print('The computer choosed {}'.format(items[computer]))
print('The player choosed {}'.format(items[jogador]))
print("-="*11)
if computer == 0: # if the computer chossed paper
    if jogador ==0:
        print("Draw")
    elif jogador ==1:
        print("Computer wins")
    elif jogador ==2:
        print("Player wins")
    else:
        print("invalid options")
elif computer == 1: # if the computer chossed rock
    if jogador ==0:
        print("Player wins")
    elif jogador ==1:
        print("Draw")
    elif jogador ==2:
        print("Computer wins")
    else:
        print("invalid options")
elif computer == 2: # if the computer chossed scissors
    if jogador ==0:
        print("Computer wins")
    elif jogador ==1:
        print("Player wins")
    elif jogador ==2:
        print("Draw")
    else:
        print("invalid options")




from random import randint
from time import sleep

print('YOU CAN´T WIN IN THIS GAME')
stake = float(input('How much is your stake?:$'))
odds = int(input("How may times do you want to win?"))
input(f'You have you win {odds} times or more to cashout at least ${odds*stake} press any key to cont')
sleep(1)
print('-=-='*30)
v = 0
final = 0
cashout = v * stake

while True:
    jogador = int(input("Insert your number"))
    computer = randint(0, 12)
    total = computer + jogador
    type= ' '
    while type not in 'EO':
      type = str(input('Even or odd [E/O] ')).strip().upper()[0]
    print(f'You played {jogador} and the computer {computer} suming up: {total} ', end=' ')
    print('It is an even number' if total%2 == 0 else 'It is an odd number')
    if type == 'E':
        if total % 2 == 0:
            print('You win')
            v+=1
        else:
            print('You lose')
            break
    elif type =='O':
        if total % 2 ==1:
            print('You win')
            v+=1
        else:
            print('You lose')
            break
    print('let´s try it again')

if v <= odds:
    print(f'You are just another noob, you won {v} times and your potential winnings is ${0} ')
else:
    print(f'You won {v} times and your potential winnings is ${v*stake}')

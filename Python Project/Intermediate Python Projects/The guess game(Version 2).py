from random import randint
computer = randint(0,10)
print("It is your computer speaking... i just thinked a number that is between 1 and 10. ")
print("can you guess it for me ?")
correct= False
attempts = 0
while not correct:
    player =  int(input("what is your attempt?: "))
    attempts += 1
    if player == computer:
        correct = True
    else:
        if player< computer:
            print('More, try again')
        elif player> computer:
            print('Less, try again')
print('You got the answer with {} attempts.'.format(attempts))

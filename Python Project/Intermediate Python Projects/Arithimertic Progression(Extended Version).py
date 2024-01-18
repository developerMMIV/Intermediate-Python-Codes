from time import sleep
print("Loading................")
sleep(1)
print("A.P Generator")
print('-='*20)
first = int(input('Digit 1:'))
reason = int(input('Reason:'))
term = first
cont = 1
total =0
mais = 10
while mais !=0:
    total = total+mais
    while cont <= total:
        print('{} ->'.format(term),end=' ')
        term += reason
        cont += 1
    print("Pause")
    mais = int(input('How many terms you want to show?:'))
print('Progression terminated with {} showed terms '.format(total))
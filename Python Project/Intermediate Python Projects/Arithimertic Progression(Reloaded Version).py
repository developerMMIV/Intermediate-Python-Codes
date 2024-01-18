from time import sleep
print("Loading................")
sleep(1)
print("A.P Generator")
print('-='*20)
first = int(input('Digit 1:'))
reason = int(input('Reason:'))
term = first
cont = 1
while cont <= 10:
    print('{} ->'.format(term),end=' ')
    term += reason
    cont += 1
print("Finished")

no1 = int(input('Primeiro Termo:'))
reason = int(input('Reason: '))
decimal = no1 + (10 - 1) * reason
for c in range(no1,decimal,reason):
    print('{} '.format(c), end='-')
print("Finished")

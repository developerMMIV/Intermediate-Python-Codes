numero = int(input("Digite o seu numero: "))
tot = 0
for c in range(1,numero+1):
    if numero % c == 0:
        print('\033[33m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mThe Number {} was dividable {} times '.format(numero, tot))
if tot == 2:
    print('The number is a prime number')
else:
    print("the number is NOT a prime number")
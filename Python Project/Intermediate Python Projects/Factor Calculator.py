n = int (input("Insert your digit:"))
c = n
f = 1
print('Calculating {}! = '.format(n),end=' ')
while c >0:
    print('{}'.format(c),end=' ')
    print('X' if c > 1 else ' = ',end= ' ')
    f *= c
    c -= 1
print('{}'.format(f))
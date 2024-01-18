ans ='Yy'
sum= quan= med = maior = menor = 0
while ans in 'Ss':
    num =int(input('Press any number:'))
    sum += num
    quan+= 1
    if quan ==1:
        maior = menor=num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor =num
    ans = str(input('Cont? [Y/N] : ')).upper().strip()[0]
med =  sum / quan
print('You pressed {} numbers and the medium is {}'.format(quan,med))
print('The largest value is {} and the smallest is {} '.format(maior,menor))
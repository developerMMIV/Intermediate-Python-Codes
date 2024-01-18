maior = 0
menor = 0

for w in range(1 , 6 ):
    weight = float(input('Weight of the  {} person: '.format(w)))
    if w == 1:
        maior=weight
        menor=weight
    else:
        if weight > maior:
            maior = weight
        if weight< menor:
           menor = weight
print('The large weight detected is {}Kg '.format(maior))
print('And the least weight detected is {}Kg'.format(menor))

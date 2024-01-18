sumofage = 0
mediaofage = 0
olderagemen = 0
nameoftheelderest = 0
totwomen20 =0
for p in range(1,5):
    print('-----{} Person -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Age:'))
    sex = str(input('Sex [M/F]:')).strip()
    sumofage+=idade
    if p ==1 and sex in 'Mn':
        olderagemen = idade
        nameoftheelderest = nome
    if sex in 'Mm' and idade > olderagemen:
        olderagemen= idade
        nameoftheelderest = nome

    if sex in 'Ff' and idade < 20:
        totwomen20+=1

mediaofage = sumofage/4
print('The age median is of {} years of age'.format(mediaofage))
print('the oldest man has {} years and his name is {} '.format(olderagemen,nameoftheelderest))
print('The rest are {} women with less of 20 years '.format(totwomen20))
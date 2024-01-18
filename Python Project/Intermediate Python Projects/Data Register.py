tot18 = 0
totW20 = 0
totM = 0
while True:
    age = int(input('Age:'))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sex M/F:')).strip().upper()[0]
    if age >= 18:
        tot18+= 1
    if sex== 'M' :
        totM += 1
    if sex == 'F' and age <=20:
        totW20+= 0
    ans = ' '
    while ans not in 'YN':
        ans = str(input("Continue? Y/N")).strip().upper()[0]
    if ans == 'N':
        break
print('Loading data............')
print(f'there are {totM} men, {tot18} people above the age of 18 and {totW20} women below the age of 20 ')

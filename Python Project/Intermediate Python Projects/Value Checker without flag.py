sum =cont = 0
while True:
    num = int(input('Insert your number '))
    if num == 1000:
        break
    cont+=1
    sum+=num
print(f'The sum was {sum} and it was {cont} numbers ')
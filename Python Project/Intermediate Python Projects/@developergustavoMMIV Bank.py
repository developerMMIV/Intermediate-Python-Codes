print('='*50)
print("{:^50}".format('THE M.M.I.V BANK'))
print('='*50)
amount = int(input('How much do you want to withdraw?'))
total = amount
note= 50
notetotal = 0
while True:
    if total>= note:
        total -= note
        notetotal+=1
    else:
        if notetotal > 0:
            print(f' {notetotal} notes  will be given to you if you withdraw ${note}')
        if note == 50:
            note = 20
        elif note == 20:
            note=10
        elif note == 10:
            note=1
        notetotal=0
        if total ==0:
            break
print("Thank you come again")



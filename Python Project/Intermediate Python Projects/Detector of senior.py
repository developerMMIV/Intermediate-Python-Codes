from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for peop in range(1,8):
    birth = int(input("Year of birth of the {} person:".format(peop)))
    age = atual- birth
    if age >= 21 :
        totmaior+=1
    else:
        totmenor+=1
print("There are {} Older people and there are {} younger people there ".format(totmaior,totmenor))



soma = 0
cont = 0

for c in range(1,7):
    num = int(input('Digite um valor:'))
    if num %2==0:
       soma = soma + num
       cont = cont + 1

#if soma % 2==0:
print("{} is an even number and you only informed {} even numbers".format(soma,cont))
#else:
    #print("{} is an odd number so therefore, i'm deleting it  ".format(soma))


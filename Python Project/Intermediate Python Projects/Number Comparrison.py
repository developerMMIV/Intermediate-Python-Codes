num1 = int(input("Digite o seu numero"))
num2 = int(input("Digite outro numero"))

if num2 > num1:
    print("{} is larger than {}".format(num2,num1))
elif num2 <num1:
    print("{} is smaller than {}".format(num2,num1))
else:
    print("{} and {} are the same".format(num1,num2))
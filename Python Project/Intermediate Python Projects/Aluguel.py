casa = float(input("Valor da casa: R$"))
salario = float(input("O seu salario R$"))
ano_de_validade = int(input("Quantos anos voce vai pagar o seu empresstimo?: "))
porcentagem = casa/(ano_de_validade*12)
minimo= salario * 30/100

if porcentagem <= minimo:
    print("para pagar a casa de {}, voce precisa pagar {:.2f} por mes para o seu {} anos de empresstimo".format(casa,porcentagem,ano_de_validade))
    print("Com o seu salario de R${}, VOCE NÃO PODE FAZER ESTE EMPRESSTIMO".format(salario))
else:
    print("para pagar a casa de {}, voce precisa pagar {:.2f} por mes para o seu {} anos de empresstimo".format(casa,porcentagem,ano_de_validade))
    print("com o seu salario de R${}, VOCE PODE FAZER ESTE EMPRESSTIMO")

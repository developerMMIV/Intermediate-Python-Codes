casa = float(input("Quanto custa o valor da casa?: R$"))
salario = float(input("Qual é o seu salario?: R$"))
anos = int(input("Quantos anos voce quer pagar o seu empresstimo por mes?:"))
prestacao = casa/(anos*12)
minimo = salario * 30 /100
print('para pagar uma casa de R$ {:.2f} em {} anos'.format(casa,anos),end=' ')
print('A prestaçao sera de R${:.2f}'.format(prestacao))
if prestacao<= minimo:
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
    
print('{:=^40}'.format(' MMIV STORES '))
preco = float(input("Digite o preco: R$"))
print(''' FORMAS DE PAGAMENTO
[ 1 ] A vista
[ 2 ] A vista no cartão
[ 3 ] Em ate 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("Qual é a sua opçao?:"))
if opcao == 1:
    total = preco- (preco * 10/100)
elif opcao == 2:
    total = preco - (preco *5/100)
elif opcao == 3:
    total = preco
    parcela = preco/2
    print("Sua compra vai ser parcelada em 2x em {:.2f} SEM JUROS".format(parcela))
elif opcao== 4:
    total = preco+ (preco *20/100)
    totparc = int(input("Quantas parcelas?: "))
    parcela = total/totparc
    print("Sua compra vai ser parcelada em {}x de {:.2f} COM JUROS".format(totparc,parcela))
else:
    total = 0
    print("Opçao errado, tente novamente")

print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(preco, total))
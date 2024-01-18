num = int(input('Digite um numero inteiro'))
print(''' Escolha uma das bases 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input("Sua opçao: "))

if opcao == 1:
    print("Numero em binario {} é {} ".format(num, bin(num) [2:]))
elif opcao ==2:
    print("Numero em octal {} é {} ".format(num, oct(num)[2:]))
elif opcao == 3:
    print("Numero em hexa {} é {} ".format(num, hex(num)[2:]))
else:
    print("numero invalido")
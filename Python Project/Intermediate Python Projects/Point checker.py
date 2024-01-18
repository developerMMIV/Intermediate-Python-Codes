nota1 = float(input("Primeira nota:"))
nota2 = float(input("Segunda nota:"))
media = (nota1+nota2)/2
if media <= 5.0:
    print("Sua nota é {}, Voce esta reprovado".format(media))
elif media <=6.9:
    print("Sua nota é {}, Voce esta em recuperaçao ".format(media))
elif media >= 7.0:
    print("Sua nota é {}, voce esta aprovado".format(media))
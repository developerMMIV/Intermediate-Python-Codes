peso = float(input("Qual é o seu peso?(Kg):"))
altura = float(input("Qual é sua altura?(m):"))
imc = peso / (altura**2)
print("Your BMI is {:.1f}".format(imc))
if imc < 18.5:
    print("you are below the average weight")
elif 18.5 <= imc <25:
    print("Congrats, you are in the average weight")
elif 25 <= imc <  30:
    print("You are above the average weight ")
elif 30 <= imc < 40:
    print("You are obese")
else:
    print(" You need go to the GYM")
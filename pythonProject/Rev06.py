peso = float(input("peso: "))
altura = float(input("altura: "))

imc = peso/(altura**2)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 < imc < 25:
    print("Peso ideal")
elif 25.0 <= imc < 30:
    print("Levemente acima")
elif 30.0 <= imc < 35:
    print("Obeso 1")
elif 35.0 <= imc < 40:
    print("Obeso 2 ")
else:
    print("Obeso 3 ")
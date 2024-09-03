num1 = float(input("Insira uma nota "))
num2 = float(input("Insira uma nota "))
num3 = float(input("Insira uma nota "))

if 10 > num1 < 0:
    if 10 >= num2 <= 0:
        if 10 >= num3 <= 0:
            media = (num1+num3+num2)/3

            if media >= 7:
                print("Aprovado")
            elif media <= 4:
                print("recuperação")
            else:
                print("reprovado")
        else:
            print("numeros invalidos")
    else:
        print("numeros invalidos")
else:
    print("numeros invalidos")
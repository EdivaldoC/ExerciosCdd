escolha = 0
while escolha == 0:
    num = int(input("Digita: "))
    if num % 2 == 0:
        if num > 0:
            print("Ele e par e positivo")
        else:
            print("Ele e par negativo")
    else:
        if num < 0:
            print("Ele e impar e negativo")
        else:
            print("Ele e impar e positivo")

    escolha = int(input("Continuar ? \n""Continuar = 0 \n""Sair = 1"))

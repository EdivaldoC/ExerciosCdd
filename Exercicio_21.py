nocao = 0
while nocao != 1:
    n1 = int(input("Dgite um valor: "))
    if n1 == 0:
            while n1 == 0:
                n1 = int(input("Digite outro valor: "))

    n2 = int(input("Dgite um valor"))
    if n2 == 0:
        while n2 == 0:
            n2 = int(input("Digite outro valor: "))
    div = n1/n2
    print(f"a divisao e: {div}")
    nocao = int(input(" finalizar = 1 \n continuar = 0 \n "))
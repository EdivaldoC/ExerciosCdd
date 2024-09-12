print("Bem vindo a calculadora")
escolha = int(input("escolha \n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar \n"))
while escolha != 5:

    match escolha:
        case 1:
            n1 = int(input("Digite um  numero: "))
            n2 = int(input("Digite um  numero: "))
            soma = n1 + n2
            print(f"A soma e: {soma}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar "))

        case 2:
            n1 = int(input("Digite um  numero: "))
            n2 = int(input("Digite um  numero: "))
            sub = n1 - n2
            print(f"A subtração e: {sub}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar "))
        case 3:
            n1 = int(input("Digite um  numero: "))
            n2 = int(input("Digite um  numero: "))
            mult = n1 * n2
            print(f"A multiplicação e {mult}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar "))
        case 4:
            n1 = int(input("Digite um  numero: "))
            if n1 == 0:
                while n1 == 0:
                    n1 = int(input("Digite outro valor: "))
            n2 = int(input("Digite um  numero: "))
            if n2 == 0:
                while n2 == 0:
                    n2 = int(input("Digite outro valor: "))
            div = n1 / n2
            print(f"A divisao e {div}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subitração \n 3 = mult \n 4 = div \n 5 = encerrar "))
        case 5:
            print("terminou")
            break

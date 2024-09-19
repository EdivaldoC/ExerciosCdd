print("Bem vindo a calculadora")
n1 = int(input("Digite um  numero: "))
n2 = int(input("Digite um  numero: "))
escolha = int(input("escolha \n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar \n 6 = digitar denovo: \n"))
while escolha != 5:
    match escolha:
        case 1:
            soma = n1 + n2
            print(f"A soma e: {soma}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar \n 6 = digitar denovo \n"))
        case 2:
            sub = n1 - n2
            print(f"A subtração e: {sub}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar \n 6 = digitar denovo \n"))
        case 3:
            mult = n1 * n2
            print(f"A multiplicação e {mult}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar \n 6 = digitar denovo \n"))
        case 4:
            if n1 == 0:
                while n1 == 0:
                    n1 = int(input("Digite outro valor: "))
            n2 = int(input("Digite um  numero: "))
            if n2 == 0:
                while n2 == 0:
                    n2 = int(input("Digite outro valor: "))
            div = n1 / n2
            print(f"A divisao e {div}")
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar \n 6 = digitar denovo \n"))
        case 5:
            print("terminou")
            break
        case 6:
            n1 = int(input("Digite um  numero: "))
            n2 = int(input("Digite um  numero: "))
            escolha = int(input("escolha de\n 1 = soma \n 2 = subtração \n 3 = mult \n 4 = div \n 5 = encerrar \n 6 = digitar denovo \n"))
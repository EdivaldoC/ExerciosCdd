deci = 0
while deci == 0:
    tome = True
    while tome:
        nota1 = int(input("Digite a primeira nota: "))
        if 0 <= nota1 <= 10:
            tome = False
            while True:
                nota2 = int(input("Digite a segunda nota: "))
                if 0 <= nota2 <= 10:
                    media = (nota1 + nota2) / 2
                    print(f"A média é: {media}")
                    break
                else:
                    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
        else:
            print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
    deci = int(input("Deseja continuar digite 0 se nao digite 1: "))
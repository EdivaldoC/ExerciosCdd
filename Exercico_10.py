hora1 = int(input("Digite a hora da primeira entrada: "))
minuto1 = int(input("Digite os minutos da primeira entrada: "))

if 0 <= hora1 < 24 and 0 <= minuto1 < 60:
    hora2 = int(input("Digite a hora da segunda entrada: "))
    minuto2 = int(input("Digite os minutos da segunda entrada: "))

    if 0 <= hora2 < 24 and 0 <= minuto2 < 60:
        somamin = minuto2 + minuto1
        somahoras = (hora2 + hora1) + 12
        print(somahoras)
        if somamin >= 60:
            somamin -= 60
            somahoras += 1

        if somahoras >= 24:
            somahoras -= 24
            print("entrei")


        print(f"A saída é {somahoras:02d}:{somamin:02d}")

    else:
        print("Hora ou minutos da segunda entrada inválidos")
else:
    print("Hora ou minutos da primeira entrada inválidos")

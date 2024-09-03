nome1 = str(input("insira o nome do time "))
gols1 = int(input("quantos gols esse time fez "))
nome2 = str(input("Insira o nome do outro time "))
gols2 = int(input("Quantos gols esse time fez "))

if gols1 > gols2:
    print(f"O time {nome1} fez {gols1} ele e o vencedor!!")
elif gols1 == gols2:
    print("Nao houve vencedor!!!")
else:
    print(f"O time {nome2} fez {gols2} ele e o vencedor!!")


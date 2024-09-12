count = 0
soma = 0
Naluno = int(input("digite a quant de aluno: "))
while count != Naluno:
    nota = float(input("digite a nota: "))
    count = count + 1
    soma = soma + nota
media = soma / Naluno
print(f"A media da sala e {media}")

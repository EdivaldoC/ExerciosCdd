quant = int(input("Digite a quantidade de aluno"))
soma = 0

for x in range(quant):
    nota = float(input(f"digite nota do {x} aluno:  "))
    soma = soma + nota
media = soma/quant
print(f"a media da turma e {media} ")

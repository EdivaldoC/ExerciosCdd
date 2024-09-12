soma = 0
for x in range(10):
    num = int(input("Digite um numero"))
    if num % 2 == 1:
        soma = num + soma
print(soma)

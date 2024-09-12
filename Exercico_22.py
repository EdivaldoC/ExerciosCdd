
cont = 0
num = 1
while cont == 0:
    n = int(input("Digite um numero"))
    while num < 11:
       mult = n * num
       print(f"{num} X {n} = {mult}")
       num = num + 1
    cont = int(input("0 continua \n 1 finaliza"))
    num = 1


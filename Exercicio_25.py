num = int(input("Digite um numero: "))
for x in range(num + 1):
    for y in range(x):
        print(y,end=" ")
    print()
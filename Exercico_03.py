nome = str(input("Dgiite seu nome: "))
print("================================")
idade = int(input("digite sua idade: "))
print("================================")
salario = float(input("digite seu salario: "))

print("================================")
salarioinc = salario * 1.10
idademe = idade * 12
print(f"Ola {nome} sua iade em meses {idademe} e que ganha {salarioinc:,.2f}")
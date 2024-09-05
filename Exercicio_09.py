Litros = float(input("litros vendidos: "))
tipo = str(input("G ou E : "))

if tipo == "G" or "g":
    valor = Litros * 5.80

elif tipo == "E" or "e":
    valor = Litros * 4.90
else:
    print("combustivel invalido")
    
print(f"O valor a ser pago e R${valor: .2f}")
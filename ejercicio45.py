mayor = 0
cantidad = int(input("Ingrese la cantidad de triangulos a analizar :"))

for x in range(cantidad):
    base = int(input("Ingrese la base :"))
    altura = int(input("Ingrese la altura :"))
    superficie = (base * altura) / 2
    print("La superficie del triangulo es :")
    print(superficie)
    if superficie > 12:
        mayor = mayor + 1
         
         
print("La cantidad mayores a 12 son :")
print(mayor)
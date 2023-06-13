mayores = 0
cantidad = int(input("Ingrese la cantidad de analizar :"))

for x in range(cantidad):
    valores = int(input("Ingrese los valores :"))
    if valores >= 1000:
        mayores = mayores + 1
print("Los valores iguales o mayores a 1000 son :")
print(mayores)
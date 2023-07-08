cuadrante1 = 0
cuadrante2 = 0
cuadrante3 = 0
cuadrante4 = 0
cantidad = int(input("Ingrese la cantidad de cordenadas a analizar :"))
for x in range(cantidad):
    x = int(input("Ingrese la cordenada x :"))
    y = int(input("Ingrese la cordenada y :"))
    if x > 0 and y > 0:
        cuadrante1 = cuadrante1 + 1
    else:
        if x < 0 and y > 0:
            cuadrante2 = cuadrante2 + 1
        else:
            if x < 0 and y < 0:
                cuadrante3 = cuadrante3 + 1
            else:
                if x > 0 and y < 0:
                     cuadrante4 = cuadrante4 + 1
print("La cantidad de cordenadas en el cuadrante 1 son :")
print(cuadrante1)
print("La cantidad de cordenadas en el cuadrante 2 son :")
print(cuadrante2)
print("La cantidad de cordenadas en el cuadrante 3 son :")
print(cuadrante3)
print("La cantidad de cordenadas en el cuadrante 4 son :")
print(cuadrante4)
            
suma_pares = 0
multiplo = 0
negativo = 0
positivo = 0

for x in range(10):
    valores = int(input("Ingrese los numeros a analizar :"))
    if valores % 2 == 0:
        suma_pares = suma_pares + valores
    if valores % 15 == 0:
            multiplo = multiplo + 1
    if valores > 0:
        positivo = positivo + 1        
    else:
        if valores < 0:
            negativo = negativo + 1
         
print("Los numeros positivos son :")
print(positivo)
print("Los numeros negativos son :")
print(negativo)
print("Los multiplos de 15 son :")
print(multiplo)
print("Los suma de los numeros pares ingresados  son :")
print(suma_pares)
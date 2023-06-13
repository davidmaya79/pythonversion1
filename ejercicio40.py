x = 1
pares = 0
impares = 0

cantidad = int(input("Ingrese la cantidad de numeros a analizar :"))
while x <= cantidad:
    numeros = int(input("Ingrese los numeros a analizar :"))
    if numeros % 2 == 0:
        pares = pares + 1
    else:
        if numeros % 2 != 0:
            impares = impares + 1
    x = x + 1
print("La cantidad de numeros pares es :")
print(pares)
print("La cantidad de numeros impares es :")
print(impares)


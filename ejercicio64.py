x = 0
cantidad = 0
oracion = input("Ingrese la oracion :")
oracion2 = oracion.lower()
while x < len(oracion2):
    if oracion2[x] == "a" or oracion2[x] == "e" or oracion2[x] == "i" or oracion2[x] == "o" or oracion2[x] == "u":
        cantidad = cantidad + 1
    x = x + 1
print("La cantidad de vocales en la oracion son :")
print(cantidad)
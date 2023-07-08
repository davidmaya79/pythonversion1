x = 0
cantidad = 0
oracion = input("Ingrese la oracion :")
while x < len(oracion):
    if oracion[x] == " ":
        cantidad = cantidad + 1
    x = x + 1
print("La cantidad de espacios que tiene la oracion es :")
print(cantidad)    

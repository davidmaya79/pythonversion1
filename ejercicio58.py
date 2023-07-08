suma = 0
opcion = "si"
while opcion == "si":
    valor = int(input("Ingrese el valor : "))
    suma = suma + valor
    opcion = input("Desea cargar otro valor (si/no)")
print("La suma de los numeros ingresados es :")
print(suma)
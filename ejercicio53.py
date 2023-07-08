suma = 0
# cantidad = int(input("Ingrese la cantidad de numeros enteros a analizar :"))
valores = int(input("Ingrese los valores :"))
while valores != -1:
    suma = suma + valores
    valores = int(input("Ingrese los valores :"))
     
     
print("La suma de todos los valores es :")
print(suma)
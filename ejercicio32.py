cantidad = int(input("Ingrese la cantidad de lotes :"))

suma = 0
x = 1

while x <= cantidad:
    longitudes = float(input("Ingrese la longitud de los perfiles :"))
    if longitudes >= 1.20 and longitudes <= 1.30:
        suma = suma + 1
    x = x + 1
    
print("La cantidad de piezas aptas que hay son :")
print(suma)

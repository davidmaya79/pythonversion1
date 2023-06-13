multiplo3 = 0
multiplo5 = 0
for x in range(10):
    numeros = int(input("Ingrese los numeros :"))
    if numeros % 3 == 0 and  numeros % 5 == 0:
        multiplo3 = multiplo3 + 1
        multiplo5 = multiplo5 + 1
    else:
        if numeros % 3 == 0:
            multiplo3 = multiplo3 + 1
        else:
            if numeros % 5 == 0:
                multiplo5 = multiplo5 + 1
print ("La cantidad de numeros multiplos de 3 son :")
print(multiplo3)
print ("La cantidad de numeros multiplos de 5 son :")
print(multiplo5)


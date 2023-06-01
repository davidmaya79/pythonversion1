x = 1
mayores = 0
menores = 0

while x <= 10:
    notas = int(input("Ingrese las 10 notas :"))
    if notas >= 7:
        mayores = mayores + 1
    else:
        menores = menores + 1
    x = x + 1
print("Las notas mayores o iguales a 7 son :")
print(mayores)
print("Las notas menores a 7 son :")
print(menores)  
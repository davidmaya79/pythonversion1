mayores = 0
menores = 0
for x in range(10):
    notas = float(input("Ingrese las notas :"))
    if notas >= 7:
        mayores = mayores + 1
    else:
        menores = menores + 1
print("Las notas mayores o iguales a 7 son :")
print(mayores)
print("Las notas  menores a 7 son :")
print(menores)
    
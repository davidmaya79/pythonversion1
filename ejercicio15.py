nota1 = int(input("Ingrese el primer valor :"))
nota2 = int(input("Ingrese el segundo valor :"))
nota3 = int(input("Ingrese el tercer valor :"))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("Promocionado")
else:
    if promedio >= 4:
        print("Regular")
    else:
        print("Reprobado")
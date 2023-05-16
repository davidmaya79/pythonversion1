nota1 = int(input("Ingrese el primer valor :"))
nota2 = int(input("Ingrese el segundo valor :"))
nota3 = int(input("Ingrese el tercer valor :"))

if nota1 > nota2:
    if nota1 > nota3:
        print("El numero mayor es :")
        print(nota1)
    else:
        print("El numero mayor es :")
        print(nota3)
else:
    if nota2 > nota3:
        if nota2 > nota3:
            print("El numero mayor es :")
            print(nota2)
        else:
            print("El numero mayor es :")
            print(nota3)
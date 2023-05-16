# Solicitar al usuario ingresar el primer valor
nota1 = int(input("Ingrese el primer valor: "))

# Solicitar al usuario ingresar el segundo valor
nota2 = int(input("Ingrese el segundo valor: "))

# Solicitar al usuario ingresar el tercer valor
nota3 = int(input("Ingrese el tercer valor: "))

# Comprobar si nota1 es mayor que nota2
if nota1 > nota2:
    # Si nota1 es mayor que nota2, comprobar si nota1 es también mayor que nota3
    if nota1 > nota3:
        # Si nota1 es mayor que nota3, imprimir que nota1 es el número mayor
        print("El número mayor es:")
        print(nota1)
    else:
        # Si nota1 no es mayor que nota3, imprimir que nota3 es el número mayor
        print("El número mayor es:")
        print(nota3)
else:
    # Si nota1 no es mayor que nota2, comprobar si nota2 es mayor que nota3
    if nota2 > nota3:
        # Si nota2 es mayor que nota3, imprimir que nota2 es el número mayor
        print("El número mayor es:")
        print(nota2)
    else:
        # Si nota2 no es mayor que nota3, imprimir que nota3 es el número mayor
        print("El número mayor es:")
        print(nota3)
                                 
                 
                                                                                          
     
            
            
# Se le pide al usuario ingresar tres números enteros y se almacenan en las variables num1, num2, y num3.
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

# Se verifica si num1 es el número mayor de los tres.
if num1 > num2 and num1 > num3:
    # Si num1 es el número mayor, se imprime "El número mayor es:" y luego se imprime num1.
    print("El número mayor es:")
    print(num1)

# Si num1 no es el número mayor, se verifica si num2 es el número mayor.
else:
    if num2 > num3:
        # Si num2 es el número mayor, se imprime "El número mayor es:" y luego se imprime num2.
        print("El número mayor es:")
        print(num2)
    else:
        # Si ni num1 ni num2 son el número mayor, entonces num3 debe ser el número mayor.
        # Se imprime "El número mayor es:" y luego se imprime num3.
        print("El número mayor es:")
        print(num3)

# Se realiza un proceso similar para encontrar el número menor.
if num1 < num2 and num1 < num3:
    # Si num1 es el número menor, se imprime "El número menor es:" y luego se imprime num1.
    print("El número menor es:")
    print(num1)
else:
    if num2 < num3:
        # Si num2 es el número menor, se imprime "El número menor es:" y luego se imprime num2.
        print("El número menor es:")
        print(num2)
    else:
        # Si ni num1 ni num2 son el número menor, entonces num3 debe ser el número menor.
        # Se imprime "El número menor es:" y luego se imprime num3.
        print("El número menor es:")
        print(num3)

num = int(input("Ingrese un número entero entre 1 y 999: "))  # Solicitar al usuario que ingrese un número entero
                                                            # y convertirlo a entero usando la función int()
if num < 10:                                               # Comprobar si el número es menor que 10
    print("El número ingresado tiene 1 cifra")              # Imprimir mensaje si el número tiene 1 cifra
else:
    if num < 100:                                          # Comprobar si el número es menor que 100
        print("El número ingresado tiene 2 cifras")         # Imprimir mensaje si el número tiene 2 cifras
    else:
        if num < 1000:                                     # Comprobar si el número es menor que 1000
            print("El número ingresado tiene 3 cifras")     # Imprimir mensaje si el número tiene 3 cifras
        else:
            print("ERROR")                                 # Imprimir "ERROR" si el número está fuera del rango válido

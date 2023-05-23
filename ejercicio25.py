# El siguiente programa solicita al usuario que ingrese tres números enteros
num1 = int(input("Ingrese el primer valor :"))
num2 = int(input("Ingrese el segundo valor :"))
num3 = int(input("Ingrese el tercer valor :"))

# Si los tres números son iguales, continúa con el siguiente bloque de código
if num1 == num2 and num1 == num3:
    # Calcula la suma de los dos primeros números
    suma = num1 + num2
    # Multiplica la suma anterior por el tercer número ingresado
    multiplicacion = suma * num3
    # Imprime la suma de los dos primeros números
    print("la suma es :")
    print(suma)
    # Imprime el resultado de la multiplicación anterior
    print("el resultado de la multiplicacion es :")
    print(multiplicacion)

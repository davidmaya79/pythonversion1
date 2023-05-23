 # Se solicita al usuario que ingrese su sueldo y antigüedad
sueldo = int(input("Ingrese su sueldo :"))
antiguedad = int(input("Ingrese su antiguedad :"))

# Se verifica si el sueldo es menor a 500 y la antigüedad es mayor o igual a 10 años
if sueldo < 500 and antiguedad >= 10:
    # Si se cumple la condición anterior, se calcula el aumento del sueldo con un 20% de incremento
    aumentoa = (sueldo * 0.20) + sueldo
    # Se muestra en pantalla el aumento del sueldo
    print("El aumento del sueldo es de ")
    print(aumentoa)
else:
    # Si no se cumple la primera condición, se verifica si el sueldo es menor a 500 y la antigüedad es menor a 10 años
    if sueldo < 500 and antiguedad < 10:
        # Si se cumple la condición anterior, se calcula el aumento del sueldo con un 5% de incremento
        aumentob = (sueldo * 0.05) + sueldo
        # Se muestra en pantalla el aumento del sueldo
        print("El aumento del sueldo es de ")
        print(aumentob)
    else:
        # Si no se cumple ninguna de las dos condiciones anteriores, se muestra el sueldo sin cambios
        if sueldo >= 500:
            print(sueldo)

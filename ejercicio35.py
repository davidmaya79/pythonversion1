cantidad_empleados = int(input("Ingrese la cantidad de empleados :"))

x = 1
# suma1 = 0
# suma2 = 0
suma_total = 0
cobro1 = 0
cobro2 = 0

while x <= cantidad_empleados:
    sueldos = int(input("Ingrese el sueldos de los trabajadores :"))
    if sueldos >= 100 and sueldos <= 300:
        cobro1 = cobro1 + 1
        # suma1 = suma1 + sueldos
    else:
         if sueldos > 300:
            cobro2 = cobro2 + 1
            # suma2 = suma2 + sueldos
    suma_total = suma_total + sueldos
    x = x + 1
    
print("Los sueldos entre 100 y 300 son :")
print(cobro1)
print("Los sueldos mayores a 300 son :")
print(cobro2)
print("El importe que paga en sueldos es :")
# suma_total = suma1 + suma2
print(suma_total)

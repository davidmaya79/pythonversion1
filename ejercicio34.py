cantidad = int(input("Ingrese la cantidad de personas :"))
x = 1
suma = 0
while x <= cantidad:
    altura = float(input("Ingrese las alturas :"))
    suma = suma + altura
    promedio = suma/cantidad
    x = x + 1
print("El promedio de la altura de los estudiantes es ")
print(promedio)    
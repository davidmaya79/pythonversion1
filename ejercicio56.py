print("Datos de la primera persona ")
nombre1 = input("Ingrese nombre :")
edad1 = int(input("Ingrese la edad :"))
altura1 = float(input("Ingrese la altura (Ej: 1.75):"))
print("Datos de la segunda persona ")
nombre2 = input("Ingrese nombre :")
edad2 = int(input("Ingrese la edad :"))
altura2 = float(input("Ingrese la altura (Ej: 1.75):"))
print("Persona mas alta ")
if altura1 > altura2:
    print(nombre1)
else:
    print(nombre2)
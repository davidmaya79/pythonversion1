suma_dia = 0
suma_tarde = 0
suma_noche = 0
for x in range(5):
    estudiantes_dia = int(input("Ingrese las edades de los estudiantes de dia :"))
    suma_dia = suma_dia + estudiantes_dia
    promedio_dia = suma_dia / 5 
    
for x in range(6):
    estudiantes_tarde = int(input("Ingrese las edades de los estudiantes la tarde :"))
    suma_tarde = suma_tarde + estudiantes_tarde
    promedio_tarde = suma_tarde / 6 
    
for x in range(11):
    estudiantes_noche = int(input("Ingrese las edades de los estudiantes de noche :"))
    suma_noche = suma_noche + estudiantes_noche
    promedio_noche = suma_noche / 11
print("El promedio de los estudiantes de dia son :") 
print(promedio_dia)
print("El promedio de los estudiantes de tarde son :") 
print(promedio_tarde)
print("El promedio de los estudiantes de noche son :") 
print(promedio_noche)

if promedio_dia > promedio_tarde and promedio_dia > promedio_noche:
    print("El promedio mayor es el de los estudiantes de dia ")
else:
    if promedio_tarde >  promedio_noche:
        print("El promedio mayor es el de los estudiantes de tarde ")
    else:
        print("El promedio mayor es el de los estudiantes de noche ")
        
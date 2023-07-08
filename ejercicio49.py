escaleno = 0
equilatero = 0
isosceles = 0
cantidad = int(input("Ingrese la cantidad de triangulos a analizar :"))

for x in range(cantidad):
    ladoa = int(input("Ingrese el primer lado del triangulo 1:"))
    ladob = int(input("Ingrese el segundo lado del triangulo 2:"))
    ladoc = int(input("Ingrese el tercer lado del triangulo 3:"))
    
    if ladoa == ladob and ladoa == ladoc:
        print("Triangulo equilatero")
        equilatero = equilatero + 1
    else:
        if ladoa == ladob or ladoa == ladoc or ladob == ladoc :
            print("Triangulo isoceles")
            isosceles = isosceles + 1
        else:
            print("Triangulo escaleno")
            escaleno = escaleno + 1
print("Cantidad de triangulos equilateros :")
print(equilatero)
print("Cantidad de triangulos isoceles :")
print(isosceles)
print("Cantidad de triangulos escalenos :")
print(escaleno)
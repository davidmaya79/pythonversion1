x = 1 
 
suma1 = 0
suma2 = 0
print("primera lista")
while x <= 15:
    lista1 = int(input("ingrese la primera lista de 15 valores :"))
    suma1 = suma1 + lista1
    x = x + 1
     
x = 1 
print("segunda lista")  
while x <= 15:
    lista2 = int(input("ingrese la primera lista de 15 valores :"))
    suma2 = suma2 + lista2
    x = x + 1
     
if suma1 > suma2:
        print("La lista mayor es la primera :")
        print(suma1)
else:
    if suma2 > suma1:
        print("La lista mayor es la segunda :")
        print(suma2)
    else:
        print("Las 2 listas son iguales ")
    


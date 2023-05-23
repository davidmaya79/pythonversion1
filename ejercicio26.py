x = int(input("Ingrese un valor entero positivo o negativo x :"))
y = int(input("Ingrese un valor entero positivo o negativo y :"))

if x > 0 and y > 0:
    print("Te encuentras en el primer cuadrante ")
else:
    if x < 0 and y > 0:
        print("Te encuentras en el segundo cuadrante ")
    else:
        if x < 0 and y < 0:
            print("Te encuentras en el tercer  cuadrante ")
        else:
            if x > 0 and y < 0:
                print("Te encuentras en el cuarto cuadrante ")
            else:
                print("Te encuentras sobre un eje")
        
        
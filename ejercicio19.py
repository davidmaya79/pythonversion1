preguntas = int(input("Ingrese la cantidad de preguntas que realizo :"))
contestadas_correctamente = int(input("Ingrese la cantidad de preguntas que contesto correctamente :"))

porcentaje =  (contestadas_correctamente * 100) / preguntas

if porcentaje >= 90:
    print("nivel maximo")
else:
    if porcentaje >= 75:
        print("nivel medio")
    else:
        if porcentaje >= 50:
                print("nivel regular")
        else:
            print("fuera de nivel")
 
    
    

 
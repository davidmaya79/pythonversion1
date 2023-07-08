email = input("Ingrese el email :")
x = 0
cantidad = 0

while x < len(email):
    if email[x] == "@":
        cantidad = cantidad + 1
    x = x + 1
if cantidad == 1:
    print("contiene solo un caracter @ ")
else:
    print("Incorrecto")
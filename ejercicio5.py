# Pedir al usuario el precio del producto
precio_Producto = int(input("Ingrese el precio del producto: "))

# Pedir al usuario la cantidad que desea comprar
cantidad = int(input("Ingrese la cantidad a llevar del producto: "))

# Calcular el precio total que el usuario debe pagar
pagar = precio_Producto * cantidad

# Imprimir el precio total en la pantalla
print("Usted debe pagar:")
print(pagar)
producto = str(input("ingrese el nombre del producto: "))
clave = int(input("ingrese la clave: "))
precio_original = int(input("ingrese el precio: "))

if clave == 1:
    dto1 = precio_original * 0.10
    precio_dto1 = precio_original - dto1
    print(f"el producto {producto} tiene un costo de {precio_original} y con el codigo de descuento {clave} te queda con un precio de {precio_dto1}")
elif clave == 2:
    dto2 = precio_original * 0.20
    precio_dto2 = precio_original - dto2
    print(f"el producto {producto} tiene un costo de {precio_original} y con el codigo de descuento {clave} te queda con un precio de {precio_dto2}")
else: print("ERROR 404 CLAVE NO ENCONTRADA")

# Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento. El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).
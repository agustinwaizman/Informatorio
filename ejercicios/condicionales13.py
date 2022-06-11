from random import randrange


precio = float(input("ingrese el monto a pagar: "))
dado = randrange(100)

if (dado < 74):
    descuento = precio * 0.15
    print(f"el precio es {precio} y el descuento es de {descuento}que corresponde a un 15%")
elif (dado >= 74):
    descuento = precio * 0.20
    print(f"el precio es {precio} y el descuento es de {descuento}que corresponde a un 20%")

# En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge al azar. Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta.
compra = int(input("ingrese el monto a pagar: "))
if compra >= 1000:
    descuento = compra * 0.15
    compra = compra - descuento
    print(f"el monto a pagar es {compra} y el descuento es de {descuento}")
else: print ("el importe es menor a $1000 por lo tanto no aplica al descuento")

# Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde.
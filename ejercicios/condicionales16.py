cantidad = int(input("ingrese la cantidad de productos: "))
precio = int(input("ingrese el importe a pagar: "))

if cantidad >= 3:
    descuento = precio * 0.20
    total = precio - descuento
    print(f"el total a pagar es {total}")
elif cantidad < 3:
    descuento = precio * 0.10
    total = precio - descuento
    print(f"el total a pagar es {total}")

# Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%.
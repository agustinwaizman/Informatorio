# Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
num3 = int(input("ingrese el tercer numero: "))

if num1 < num2 and num1 < num3:
    print("el primer numero es menor")
elif num1 > num2 and num1 < num3:
    print(f"{num1} es mayor que {num2} pero es menor que {num3}")
elif num1 < num2 and num1 > num3:
    print(f"{num1} es mayor que {num3} pero es menor que {num2}")
else: print(f"{num2} y {num3} son menores que {num1}")
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

if num1 == num2:
    multiplicacion = num1 * num2
    print(multiplicacion)
elif num1 > num2:
    resta = num1 - num2
    print(resta)
else:
    suma = num1 + num2
    print(suma)

# Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.
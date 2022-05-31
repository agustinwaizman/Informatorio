# Desarrolle un programa que permita determinar si un número X ingresado es par o impar.

num = int(input("ingrese un numero: "))

if num %2 == 0:
    print("el numero ingresado es par")
elif num%2 != 0:
    print("el numero ingresado es impar")
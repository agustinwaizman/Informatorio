
# Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m

m = int(input("ingrese un numero: "))
n = int(input("ingrese otro numero: "))

if m % n == 0:
    print("n es divisor de m")
else: print ("no es divisor")
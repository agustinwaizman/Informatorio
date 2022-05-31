a= int(input("ingrese un numero: "))
b= int(input("ingrese un segundo numero: "))
c= int(input("ingrese un tercer numero: "))

if (a > b and b > c):
    print(a, b, c)
elif (a > c and c > b):
    print(a, c, b)
elif (b > a and a > c):
    print(b, a, c)
elif (b > c and c > a): 
    print(b, c, a)
elif (c > a and a > b):
    print(c, a, b)
elif (c > b and b > a):
    print(c, b, a)
else: print("son iguales")

# Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
# Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, de acuerdo a los siguientes casos. Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:
# Si A>=B + C à No se trata de un triángulo
# Si A2 = B2 + C2 à Es un triángulo rectángulo
# Si A2 > B2 + C2 à Es un triángulo obtusángulo
# Si A2 < B2 + C2 à Es un triángulo acutángulo

a = int(input("Ingrese el lado 1: "))
b = int(input("Ingrese el lado 2: "))
c = int(input("Ingrese el lado 3: "))

if a >= b + c:
    print("No se trata de un triangulo")
elif a**2 == b**2 + c**2:
    print("Es un triangulo rectangulo")
elif a**2 > b**2 + c**2:
    print("Es un triangulo obtusangulo")
elif a**2 < b**2 + c**2:
    print("Es un triangulo acutangulo")
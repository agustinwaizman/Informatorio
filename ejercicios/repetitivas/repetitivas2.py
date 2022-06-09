plus = 0
suma = 0
n = int(input("ingrese un numero: "))

for i in range(1, n + 1):
    suma = i**2
    plus += suma
    print(f"el cuadrado de {i} es {suma}")

print(f"la suma de los cuadrados de los {n} numeros naturales es {plus}")

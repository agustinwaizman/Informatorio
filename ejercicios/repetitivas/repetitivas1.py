# Determinar el numero mayor de 10 numeros ingresados.

mayor = 0
for nro in range(1,11):
    valor = int(input(f"ingrese el numero {nro}: "))
    if valor > mayor:
        mayor = valor

print(f"El numero mayor de todos los ingresados es: {mayor}")
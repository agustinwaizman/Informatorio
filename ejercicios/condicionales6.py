
sueldo = int(input("ingrese su sueldo: "))

if sueldo >= 0 and sueldo < 6000:
    aumento = sueldo * 0.15
    sueldo =  aumento + sueldo
    print(f"su sueldo este mes sera de {sueldo}")
elif sueldo >= 6000 and sueldo < 7900:
    aumento = sueldo * 0.10
    sueldo = aumento + sueldo
    print(f"su sueldo este mes sera de {sueldo}")
elif sueldo >= 7900 and sueldo < 12000:
    aumento = sueldo * 0.06
    sueldo = aumento + sueldo
    print(f"su sueldo este mes sera de {sueldo}")
elif sueldo > 12000:
    print("usted no califica para este aumento")
else: print("error")

# Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:
# Sueldo Actual (en $)    Aumento
# 0 – 6000		15%
# 6000 – 7900	   10%
# 7900 – 12000	6%
# Más de 12000	 0%
# Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado.
inversor1 = int(input("ingrese la cantidad del primer inversor: "))
inversor2 = int(input("ingrese la cantidad del segundo inversor: "))
inversor3 = int(input("ingrese la cantidad del tercer inversor: "))

total_inversion = inversor1 + inversor2 + inversor3

porcentaje1 = inversor1 * 100 / total_inversion
porcentaje2 = inversor2 * 100 / total_inversion
porcentaje3 = inversor3 * 100 / total_inversion

print(f"el porcentaje del primer inversor es {porcentaje1}, el del segundo es {porcentaje2} y el del tercero es {porcentaje3}")

# Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.

horas = int(input("ingrese las horas: "))

if horas >= 40:
    extra = horas - 40
    pgoextra = extra * 20
    basico = 40 * 16
    salariohsextra = basico + pgoextra
    print(f"su salario es de: {salariohsextra}")
elif horas < 40:
    salario = horas * 16
    print(f"su salario es de {salario}")

# Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
# i. Si trabaja 40 horas o menos se le paga $16 por hora
# ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
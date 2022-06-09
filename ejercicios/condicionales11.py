cantidad_notas=int(input("ingrese la cantidad de notas a promediar: "))
i=1
suma=0
while (i <= cantidad_notas):
    nota = float(input(f"ingrese su nota numero {i}: "))
    i+=1
    suma = suma + nota
promedio = suma / cantidad_notas
print(f"el promedio es {promedio}")

# Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario

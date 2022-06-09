presupuesto = int(input("ingrese el presupuesto: "))

presup_pediatria = presupuesto * 0.60
presup_traumato = presupuesto * 0.20
presup_kinesio = presupuesto * 0.20
print(f"el presupuesto total es {presupuesto} y se reparte {presup_pediatria} para pediatria, {presup_traumato} para traumatologia y {presup_kinesio} para kinesiologia")

# En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital se reparte conforme a la sig. tabla:
# ÁREA 		PORCENTAJE
# Pediatría 60%
# Traumatología 20%
# Kinesiología 20%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado.
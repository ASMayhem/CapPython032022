jornada = 48
costoHora = 1.5
costoExtra = 3

horasTrabajadas = int(input("Ingrese sus horas trabajadas: "))

if horasTrabajadas<=jornada:
    pago = horasTrabajadas*costoHora
else:
    pago = jornada*costoHora + (horasTrabajadas-48)*costoExtra

print("Su pago es de",pago)
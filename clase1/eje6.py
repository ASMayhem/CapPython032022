sexo = "f"
edad = 54
aniosSer = 25
cotizaciones = 750
##
if cotizaciones>=750 and aniosSer>=25:
    if (sexo == "m" and edad>=60) or (sexo == "f" and edad>=55):
        print("Califica para ser jubilado")
    else:
        print("No califica para ser jubilado")
else:
    print("No califica para ser jubilado")
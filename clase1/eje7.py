from random import randint

zonaUsuario = int(input("Ingrese la zona de tiro: "))
zonaPortero = randint(1,6)
print("El portero a cubierto la zona:",zonaPortero)
if zonaUsuario==zonaPortero:
    print("No ha sido un gol")
else:
    print("Gooooool de papito maradona")
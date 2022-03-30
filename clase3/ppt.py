from random import randint

def ppt(opcion):
    if opcion==1:
        r="piedra"
    elif opcion==2:
        r="papel"
    elif opcion==3:
        r="tijera"
    return r

ganadas = 0

while ganadas<3:
    opUsuario = int(input("Ingrese una opcion:\n1.-Piedra\n2.-Papel\n3.-Tijera\n"))
    if opUsuario<1 or opUsuario>3:
        continue
    opMaquina = randint(1,3)
    opUsuario = ppt(opUsuario)
    opMaquina = ppt(opMaquina)
    print("El usuario ha seleccionado:",opUsuario)
    print("La maquina ha seleccionado:",opMaquina)
    if (opUsuario=="piedra" and opMaquina=="tijera") or (opUsuario=="papel" and opMaquina=="piedra") or (opUsuario=="tijera" and opMaquina=="papel"):
        print("El usuario gana")
        ganadas+=1
    elif opUsuario==opMaquina:
        print("Es un empate")
    else:
        print("La maquina gana")
    print("El usuario ha ganado:",ganadas,"\n")
        
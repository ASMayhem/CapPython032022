saldo = 0
op = 0
while op!=3:
    op = int(input("Ingrese una opcion: \n1.-Depositar\n2.-Retirar\n3.-Salir\n"))
    if op==1:
        saldo+=float(input("Ingrese cantidad a depositar: "))
        print("Depositado\n")
    elif op==2:
        saldo-=float(input("Ingrese cantidad a retirar: "))
        print("Retirado\n")
    elif op==3:
        print("Saliendo...\n")
    else:
        print("Opcion no valida\n")
print("Su saldo total es de:",saldo)

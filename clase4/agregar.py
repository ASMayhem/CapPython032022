dic = {}

v = True
while v:
    op = int(input("1.-Ingresar informacion\n2.-Salir\n"))
    if op==1:
        clave = input("¿Que informacion decea agregar? ")
        tipo = int(input("Elija un tipo de dato\n1.-Entero\n2.-Decimal\n3.-String\n4.-Lista\n"))
        if tipo==1:
            valor = int(input("Ingrese el valor: "))
        elif tipo==2:
            valor = float(input("Ingrese el valor: "))
        elif tipo==3:
            valor = input("Ingrese el valor: ")
        else:
            print("Opcion invalida")
        dic[clave] = valor
    elif op==2:
        v=False
    else:
        print("Opcion invalida")
    print("\n",dic,"\n")

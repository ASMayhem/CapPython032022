def mostrarProductos(dic):
    claves = dic.keys()
    for k in claves:
        print("-",k)
dic = {}
costo = 0
v = True
while v:
    op = int(input("1.-Ingresar producto\n2.-Generar factura\n3.-Salir\n"))
    if op==1:
        clave = input("Ingrese el nombre del producto: ")
        valor = float(input("Ingrese el valor unitario: "))
        dic[clave] = valor
    if op==2:
        facturar = True
        while facturar:
            opf = int(input("Facturacion\n1.-Agregar\n2.-Salir\n"))
            if opf==1:
                print("Productos disponibles")
                mostrarProductos(dic)
                indice = input("Escoja un producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                if dic.get(indice) is None:
                    print("producto no encontrado")
                    continue
                costo += dic.get(indice)*cantidad
                print("Costo:",costo)
            elif op==2:
                facturar=False
                print("Costo final:",costo)
                costo = 0
            print()
    elif op==3:
        v=False
    else:
        print("Opcion invalida")
    print("\n",dic,"\n")
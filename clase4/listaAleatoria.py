from random import randint

def imprimirTabla(tabla):
    for lista in tabla:
        print("[",end="")
        for item in lista:
            print("%3d"%item,end="")
        print(" ]")

def llenarTablaSimetrica(n):
    tabla = []
    num = 1
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[num]
            num+=1
    return tabla

def llenarTablaAsimetrica(filas):
    tabla = []
    columnas = randint(1,10)
    num = randint(1,10)
    for i in range(filas):
        tabla.append([])
        for j in range(columnas):
            tabla[i]+=[num]
            num = randint(1,10)
        columnas = randint(1,10)
    return tabla

# tabla = llenarTablaSimetrica(10)
# imprimirTabla(tabla)
# tabla = llenarTablaAsimetrica(10)
# imprimirTabla(tabla)


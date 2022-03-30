def imprimirTabla(tabla):
    for lista in tabla:
        print("[",end="")
        for item in lista:
            print("%3s"%item,end="")
        print(" ]")

def llenarTabla(n):
    tabla = []
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[" "]
    return tabla

def asterisco(tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla)):
            if i==len(tabla)//2 or j==len(tabla)//2 or (i+j)==(len(tabla)-1):
                tabla[i][j]=1
        tabla[i][i]=1
tabla = llenarTabla(11)
asterisco(tabla)
imprimirTabla(tabla)
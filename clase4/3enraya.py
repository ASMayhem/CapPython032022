from random import randint

def imprimirTablero(tablero):
    for fila in tablero:
        print("|",end="")
        for columna in fila:
            print("%2s |"%(columna),end="")
        print()

def generarTablero():
    tablero = []
    for i in range(3):
        tablero.append([])
        for j in range(3):
            tablero[i].append(" ")
    return tablero

def turnoMaquina():
    return randint(1,9)

def traductor(n):
    x = 0
    y = 0
    if n==1:
        return x,y
    else:
        n=n-1
        x = n//3
        y = n%3
        return x,y

def comprobarGanador(tabla,simbolo):
    win = True
    win2 = True
    aux = len(tabla)-1
    for i in range(len(tabla)):
        # Diagonal principal
        win = tabla[i][i]==simbolo and win
        # Diagonal secundaria
        win2 = tabla[i][aux]==simbolo and win2
        aux-=1
        # Filas
        win3 = tabla[i].count(simbolo)==3
        if win3:
            break
        #Columnas
        win4 = True
        for j in range(len(tabla[0])):
            win4 = tabla[j][i]==simbolo and win4
        if win4:
            break
    # Return
    if win or win2 or win3 or win4:
        return True
    else:
        return False

def comprobarVacio(tabla,x,y):
    if tabla[x][y]==" ":
        return True
    else:
        return False

def comprobarLleno(tabla):
    cont = 0
    for fila in tabla:
        for columna in fila:
            if columna!=" ":
                cont+=1
    if cont>=9:
        return True
    else:
        return False


tablero = generarTablero()
# tablero = [[" "," "," "],
#            [" "," "," "],
#            [" "," "," "]]
play = True
turno = randint(0,1)
imprimirTablero(tablero)
while(play):
    
    if turno==0:
        puesto = False
        posUsuario = input("Ingrese la posicion: ")
        x,y = traductor(int(posUsuario))
        if not comprobarVacio(tablero,x,y):
            print("La posicion esta ocupada")
            imprimirTablero(tablero)
            while not puesto:
                posUsuario = input("Ingrese la posicion: ")
                x,y = traductor(int(posUsuario))
                if not comprobarVacio(tablero,x,y):
                    print("La posicion esta ocupada")
                else:
                    tablero[x][y]="x"
                    puesto=True
                imprimirTablero(tablero)
        else:
            tablero[x][y]="x"
            imprimirTablero(tablero)
        turno = 1
    else:
        print()
        puesto = False
        a,b = traductor(turnoMaquina())
        if not comprobarVacio(tablero,a,b):
            while not puesto:
                a,b = traductor(turnoMaquina())
                if comprobarVacio(tablero,a,b):
                    tablero[a][b]="o"
                    puesto=True
                    imprimirTablero(tablero)                   
        else:
            tablero[a][b]="o"
            imprimirTablero(tablero)
        turno = 0
        
    if comprobarGanador(tablero,"x"):
        print("El usuario gana")
        play=False
    elif comprobarGanador(tablero,"o"):
        print("La maquina gana")
        play=False
    elif comprobarLleno(tablero):
        print("Es un empate")
        play=False
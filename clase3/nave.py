lista = [80,34,80,23,70]
capacidad = 150
pesoMax = 0
for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        suma = lista[i]+lista[j]
        if suma<=capacidad:
            print("Peso de",lista[i],"+",lista[j],"=",suma)
            if suma>pesoMax:
                pesoMax=suma
print("el peso maximo posible es:",pesoMax)
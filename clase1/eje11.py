def aniosBisiestos(inicio, fin):
    v = False
    r = "Los anio bisientos entre " + str(inicio)+" y "+str(fin)+" son: "
    for anio in range(inicio,fin+1):
        if (anio%4==0 and anio%100!=0) or anio%400==0:
            v = True
            r = r + str(anio) +", "
    if not v:
        r = "No hay años bisiestos entre " + str(inicio)+" y "+str(fin)
    return r



anioInicio = 1500
anioFin = 2022
print(aniosBisiestos(anioInicio,anioFin))


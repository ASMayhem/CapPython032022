def vecesLetra(carac,frase):
    cont = 0
    for letra in frase:
        if letra == carac:
            cont+=1
    return cont

frase = "saoko papi saoko"
carac = "o"

print("La letra: "+carac+" se repite "+str(vecesLetra(carac,frase))+" veces en la frase: "+frase )
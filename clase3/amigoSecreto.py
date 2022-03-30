from random import randint

def llenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
    return lista

def llenarAle(n):
    lista=[]
    num = randint(1,10)
    lista+=[num]
    for i in range(n-1):
        while num in lista:
            num = randint(1,10)
        lista+=[num]
    return lista
            

n = 10
lista = llenarSec(n)
lista2 = llenarAle(n)
print(lista)
print(lista2)
for i in range(len(lista)):
    print("Pareja",i,":",lista[i],"y",lista2[i])
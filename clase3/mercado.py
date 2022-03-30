lista1 = [1,2,5,3,7]
print(lista1)
while len(lista1)!=0:
    elem = int(input("ingrese la posiscion del elemento que desea eliminar: "))
    if elem > len(lista1)-1:
        print("el elemento esta fuera del rango")
    else:
        del(lista1[elem])
    print(lista1)
def prom(lista):
    suma = 0
    if len(lista)>0:
        for nota in lista:
            suma+=nota
        return suma/len(lista)
    else:
        return 0

def agegarEstudiante(dic,codigo,nombre):
    dic[codigo] = []
    dic[codigo].append(nombre)
    dic[codigo].append([])

def agregarNota(dic,codigo,nota):
    dic[codigo][1]+=[nota]

def imprimir(dic):
    for k in dic:
        print(k,dic[k])

dic = {'001':['kevin',[10,9,8,7]]}
agegarEstudiante(dic,'002','Byron')


menu = True

while menu:
    imprimir(dic)
    op = int(input("Ingrese opcion:\n1.-Agregar estudiante\n2.-Consultar\n3.-Agregar nota\n4.-Salir\n"))
    if op == 1:
        codigo = input("Ingrese codigo: ")
        nombre = input("Ingrese nombre: ")
        agegarEstudiante(dic,codigo,nombre)
    if op == 2:
        codigo = input("Ingrese codigo: ")
        print(codigo,dic[codigo],"Promedio",prom(dic[codigo][1]))
    if op == 3:
        codigo = input("Ingrese codigo: ")
        nota = float(input("Ingrese nota: "))
        agregarNota(dic,codigo,nota)
        print(codigo,dic[codigo],"Promedio",prom(dic[codigo][1]))
    if op==4:
        menu=False
    print()
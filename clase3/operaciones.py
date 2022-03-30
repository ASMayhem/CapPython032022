from random import randint
import re


v = True
while v:
    op = randint(1,4)
    cant1 = randint(1,10)
    cant2 = randint(1,10)
    if op==1:
        res = cant1 + cant2
        print(cant1,"+",cant2,"=",end="")
    elif op==2:
        res = cant1 - cant2
        print(cant1,"-",cant2,"=",end="")
    elif op==3:
        res = cant1 * cant2
        print(cant1,"*",cant2,"=",end="")
    elif op==4:
        res = cant1 // cant2
        print(cant1,"//",cant2,"= ",end="")
    else:
        print("Opcion no valida")
        continue
    userRes = int(input())
    if userRes==res:
        print("Correcto")
    else:
        print("Incorrecto")
        v=False
    print()
def triangulo(altura):
    espacios = altura
    for i in range(altura):
        for j in range(espacios):
            print("  ",end="")
        for k in range(i*2+1):
            print("* ",end="")
       
        espacios-=1
        print()

def triangulo1(altura):
    espacios = altura
    numCarac = 1
    for i in range(altura):
        for j in range(espacios):
            print("  ",end="")
        for k in range(numCarac):
            print("* ",end="")
        print()
        numCarac+=2
        espacios-=1

altura = 5
triangulo(altura)
numero = 7
r = "los divisores de "+str(numero)+" son: "
for i in range(1,numero//2+1):
    if numero%i==0:
        r+= str(i) +", "
r+= str(numero)
print(r)
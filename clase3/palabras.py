lista1 = ["a","b","c","d"]
lista2 = ["c","d","e","f"]
soloL1 = []
soloL2 = []
l1l2 = []

for item in lista1:
    if item in lista2:
        l1l2 += [item]
    else:
        soloL1 = soloL1 + [item]
for item in lista2:
    if item not in lista1:
        soloL2 = soloL2 + [item]
print(lista1)
print(lista2)
print(soloL1)
print(soloL2)
print(l1l2)
lista = [1,6,3,6,7,7,2]
# print(lista)
# for i in range((len(lista)-1),-1,-1):
#     if lista[i] in lista[:i]:
#         del(lista[i])
# print(lista)

print(lista)
for i in range((len(lista)-1),-1,-1):
    for j in range(i):
        if lista[i]==lista[j]:
            del(lista[i])
print(lista)
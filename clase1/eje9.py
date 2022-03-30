a = 10
b = 3

print("La ecuacion es: "+str(a)+"x + "+str(b)+" = 0")
if a==b==0:
    r ="infinitas soluciones"
elif a==0:
    r = "no existe solucion"
else:
    r = "La solucion es: " + str(-b/a)

print (r)
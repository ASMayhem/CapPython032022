correcto = int(input("ingrese la cantidad de aciertos: "))
incorrecto = int(input("ingrese la cantidad de errores: "))
total = correcto + incorrecto
pcorrecto = (100/total)*correcto
pincorrecto = (100/total)*incorrecto
print("Su puntaje final fue de:",str(correcto)+"/"+str(total)," ")
print("con un porcentaje de aciertos de:",pcorrecto,"y un porcentaje de errores de:",pincorrecto)
print("hola %.2f")
from ast import For


peso = float(input("ingrese su peso en kg: "))
estatura = float(input("ingrese su estatura en metros: "))
imc = peso/estatura**2
print("Su indice de masa corporal es: %3.2f"%(imc))
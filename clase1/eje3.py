dias = int(input("Ingrese el numero de dias: "))
anios = dias//365
meses = (dias%365)//30
dias2 = (dias%365)%30
print(dias,"días equivalen a",anios,"años,",meses,"meses y",dias2,"días")
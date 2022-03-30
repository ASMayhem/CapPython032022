vasos = 125
unidad = 4
total = 0
print("Cantidad de vasos",vasos,"unidad",unidad,"recicladosT:",total)
while vasos>unidad:
    reciclados = vasos//unidad
    sobran = vasos%unidad
    total+=reciclados
    vasos = reciclados + sobran
    print("Cantidad de vasos",vasos,"reciclados",reciclados,"sobran",sobran,"recicladosT:",total)
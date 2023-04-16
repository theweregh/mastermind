edad = int(input("ingrese su edad "))
tipo_de_carnet = input("ingrese su tipo de carnet (e = para estudiante /p pensionista /f familia numerosa /n nada ")
if (25<=edad<=35  and tipo_de_carnet=="e") or (0<edad<=10)\
        or (edad>=65 and tipo_de_carnet=="p") or (tipo_de_carnet=="f"):
    print("descuento del 25%")
else:
    print("no se te aplica el descuento")

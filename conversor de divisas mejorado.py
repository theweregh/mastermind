#conversor de divisas mejorado class 12
gbptoeur = 1.13
usdtoeur = 0.94
divisa = (input("¿que desea hacer?\n"
                "a) convertir libra a euro \n"
                "b) convertir euro a libra\n"
                "c) convertir dolar a euro\n"
                "d) convertir euro a dolar\n"))
texto = "introdusca la cantidad {} a convertir "
if divisa == "a" :
    vlr = float(input(texto.format("euros")))
    print("su cantidad de euros es: {}".format(vlr*gbptoeur))
elif divisa == "b":
    vlr = float(input(texto.format("libras")))
    print("su cantidad de libras es:{}".format(vlr/gbptoeur))
elif divisa == "c":
    vlr = float(input(texto.format("dolares")))
    print("su cantidad de dolares es:{}".format(vlr*usdtoeur))
elif divisa == "d":
    vlr = float(input(texto.format("euros")))
    print("su cantidad de euros es:{}".format(vlr/usdtoeur))
else:
    print("no ha eligido una obcion valida")

texto_usuario = input("ingrese un texto \n")
punto = 0
coma = 0
espacio = 0
for letra in texto_usuario:
    if letra == " ":
        espacio += 1
    elif letra == ",":
        coma += 1
    elif letra == ".":
        punto += 1
print("espacios {}, comas {},puntos {}\n".format(espacio,coma,punto))

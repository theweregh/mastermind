lista_de_compra = []
print("Programa lista de compra\n"
      "Bienvenido\n")
compra = None
while compra != "Q" :
    compra = input("¿Que desea comprar? (Q) \n")
    if compra in lista_de_compra:
        print("{} ya se encuentra en la lista".format(compra))
    else:
        if compra != "Q":
            if input("¿seguro que quieres añadir {} a la lista? [S/N]".format(compra)) == "S":
                lista_de_compra.append(compra)
            else:
                print("no se añadio ningun producto a la lista")
print("la lista de compra es {}".format(lista_de_compra))
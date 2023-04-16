lista_de_numero = []
anadir_un_numero = None
while anadir_un_numero != "Q" :
    anadir_un_numero = input("Quiere añadir un numero a la lista [S]para seguir y [Q] para salir ")
    if anadir_un_numero == "S" :
        numero = int(input("ingrese un numero "))
        if numero in lista_de_numero :
            print("el numero ya esta en la lista ")
        else:
            if anadir_un_numero != "Q":
                if input("desea añadir este numero [Y]ES [N]0 ") == "Y":
                    lista_de_numero.append(numero)
if lista_de_numero != None:
    print("el numero menor es: {} \n"
          "el numero menor es: {}".format(min(lista_de_numero),max(lista_de_numero)))

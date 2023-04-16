#ios o android
so = input("que so quieres\n"
           "a) ios\n"
           "b) android\n")
telefono_ideal = "ninguno"
if so == "a": #has elegido iod
    opcion = input("¿tienes dinero?\n"
                 "a) si\n"
                 "b) no\n")
    if opcion == "a":#tiene dinero?
        telefono_ideal = "iphone ultra pro max"
    else :
        telefono_ideal = "iphone de segunda mano"
elif so == "b":#has elegifo android
    opcion = input("¿tienes dinero?\n"
                 "a) si\n"
                 "b) no\n")
    if opcion == "a":#tiene dinero
        opcion = input("te importa la camara del movil\n"
                    "a) si\n"
                    "b) no\n")
    else :#no tiene dinero
        telefono_ideal = "android chino 100eur"
        if opcion == "a":#te importa la camara?
            telefono_ideal = "google pixel suprecamara"
        else:#no le importa la calidad de la camara
            telefono_ideal = "android calidad-precio"
print("tu movil ideal es " + telefono_ideal)
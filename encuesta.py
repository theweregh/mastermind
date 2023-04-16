titulo = "encuesta sobre la ciberseguridad "
print(titulo,"\n",
      len(titulo)*"_","\n")
puntaje = 0
opcion = input("1.¿Qué tanto conocimiento tienes sobre ciberseguridad? \n"
      "a) Mucho \n"
      "b) Algo \n"
      "c) Poco o nada \n")
if opcion == "a" :
    puntaje += 10
elif opcion == "b" :
    puntaje += 5
elif opcion == "c" :
    puntaje += 0
else:
    print("las opciones posibles son a,b y c")
    exit()
input("2.¿Crees que la ciberseguridad es importante para la protección de tus datos personales? \n"
      "a) Sí, es muy importante \n"
      "b) Es importante, pero no tanto como otros aspectos de mi vida digital \n"
      "c) No, no es importante para mí\n")
if opcion == "a" :
    puntaje += 10
elif opcion == "b" :
    puntaje += 5
elif opcion == "c" :
    puntaje += 0
else:
    print("las opciones posibles son a,b y c")
    exit()
input("3.¿Has sido víctima de algún ciberataque alguna vez? \n"
      "a) Sí \n"
      "b) No estoy seguro/a \n"
      "c) No\n")
if opcion == "a" :
    puntaje += 10
elif opcion == "b" :
    puntaje += 5
elif opcion == "c" :
    puntaje += 0
else:
    print("las opciones posibles son a,b y c")
    exit()
if puntaje >= 25:
    print("sabes mucho de ciberseguridad, felicidades \n")
elif puntaje >=15:
    print("sabes algo de ciberseguridad \n")
elif puntaje <15:
    print("no sabes nada de ciberseguridad, deberias investigar sobre este tema es interesante \n")
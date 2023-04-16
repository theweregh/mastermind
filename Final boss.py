import random
objeto = False
camino = input("Estas en un laberinto en el cual deberas escapar de un demonio \n"
               "¿Qué camino escoges?\n"
               "(a) camino a,o (b) camino b\n")
if camino == "a":
    camino = input("vas corriendo y derrepente te encuestras con una caja misterios\n"
                 "¿Qué haces?\n"
                 "La quieres abrir(s) o no (n)\n")
    if camino == "s":
        print("Felicidades obtuviste una moneda de oro\n")
        objeto = True
    else:
        objeto = False
    print("Sigues corriendo pero depronto ves unos guardias y debes de pagar una moneda "
                   "de oro para salir del laberinto\n")
    if objeto == True:
        print("Menos mal y obtuviste una moneda, se la das a los guardias y sales exitosamente del laberinto\n")
    else:
        camino = input("Que mal no tienes ninguna moneda\n"
                       "¿Por cual camino deseas seguir?\n"
                       "camino c (c) o camino d (d)\n")
        if camino == "c":
            print("corres desesperadamente del demonio que no te percatas del la piscina de la va y "
                  "termina callendo en ella\n"
                  "GAME OVER")
        else:
            print("Al parecer no puedes escapar del demonio, finalmente este te acorrala y te atrapa\n"
                  "GAME OVER")
else:
    camino = input("Sigues adelante pero ves una casa \n"
          "¿Queres entrar a la casa?\n"
          "si (s) o no (n)\n")
    if camino == "s":
        numero_random = random.randint(1, 100)
        operacion_matematica = int(input("entras a la casa y te encuentras con un mago el cual sabe el camino a la salida"
                                     ", dependiendo de como le caigas el mago te guiara a la salida o no\n"
                                     "la pregunta es:\n"
                                     "cuanto es 13*{}\n".format(numero_random)))
        if operacion_matematica == numero_random * 13:
            print("al mago no le gusta a los cerebritos y te termina mandando a un callejon sin salida\n"
                  "GAME OVER\n")
        else:
            print("Felicidad al mago no le gustaban los cerebritos y como no respondiste bien le agradaste mucho\n"
                  "El mago te teletrasporta a la salida \n")


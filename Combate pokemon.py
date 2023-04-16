from random import randint
import os
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
TAMANO_BARRA_DE_VIDA = 20
vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
BOLA_VOLTIO = 10
ONDA_TRUENO = 11
PLACAJE = 10
PISTOLA_DE_AGUA = 12
BURBUJA = 9
while vida_pikachu > 0 and vida_squirtle > 0 :
    #se desenvuelven los turnos de combate
    # turno pikachu
    print("Turno de pikachu")
    ataque_de_pikachu = randint(1,2)
    if ataque_de_pikachu == 1 :
        #bola voltio
        print("pikachu ataca con bola voltio")
        vida_squirtle -= BOLA_VOLTIO
    else:
        print("pikachu ataca con onda trueno")
        vida_squirtle -= ONDA_TRUENO
    if vida_squirtle <= 0:
        vida_squirtle = 0
        barra_de_vida_squirtle = 0
    else:
        barra_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA_DE_VIDA / VIDA_INICIAL_PIKACHU)
        barra_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA_DE_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("La vida de pikachu  es: [{}{}]({}/{})".format(barra_de_vida_pikachu*"*",
                                                         " "*(TAMANO_BARRA_DE_VIDA-barra_de_vida_pikachu),
                                                         vida_pikachu,VIDA_INICIAL_PIKACHU))
    print("la vida de squirtle es: [{}{}]({}/{})".format(barra_de_vida_squirtle * "*",
                                                         " "*(TAMANO_BARRA_DE_VIDA-barra_de_vida_squirtle),
                                                         vida_squirtle,VIDA_INICIAL_SQUIRTLE))
    input("presiona ENTER para continuar...\n")
    os.system("cls")
    #turno squirtle
    if vida_squirtle > 0:
        print("turno squirtle")
        ataque_squirtle = None
        while ataque_squirtle != "p" and ataque_squirtle != "a" and ataque_squirtle != "b" and ataque_squirtle != "n":
             ataque_squirtle = input("¿Qué ataque desea realizar? [p]lacaje, Pistola [a]gua, [b]urbuja, [n]o hacer nada :\n")
             if  ataque_squirtle == "p":
                 vida_pikachu -= PLACAJE
             elif ataque_squirtle == "a":
                 vida_pikachu -= PISTOLA_DE_AGUA
             elif ataque_squirtle == "b":
                 vida_pikachu -= BURBUJA
             elif ataque_squirtle == "n":
                 print("squirtle no hace nada...")
        if vida_pikachu <= 0:
            vida_pikachu = 0
            barra_de_vida_pikachu = 0
        if vida_squirtle <= 0:
            vida_squirtle = 0
            barra_de_vida_squirtle = 0
        else:
            barra_de_vida_pikachu = int(vida_pikachu*TAMANO_BARRA_DE_VIDA/VIDA_INICIAL_PIKACHU)
            barra_de_vida_squirtle = int(vida_squirtle*TAMANO_BARRA_DE_VIDA/VIDA_INICIAL_SQUIRTLE)
        print(
            "La vida de pikachu  es: [{}{}]({}/{})".format(barra_de_vida_pikachu * "*",
                                                           " " * (TAMANO_BARRA_DE_VIDA - barra_de_vida_pikachu),
                                                       vida_pikachu, VIDA_INICIAL_PIKACHU))
        print("la vida de squirtle es: [{}{}]({}/{})".format(barra_de_vida_squirtle * "*",
                                                         " " * (TAMANO_BARRA_DE_VIDA - barra_de_vida_squirtle),
                                                         vida_squirtle, VIDA_INICIAL_SQUIRTLE))
        input("presiona ENTER para continuar...\n")
        os.system("cls")
if vida_pikachu > vida_squirtle :
    print("pikachu gana!")
else:
    print("squirtle gana!")
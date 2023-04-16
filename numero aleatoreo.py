import random
na = random.randint(1,10)
nu = int(input("ingrese un numero de 1 a 10 "))
if nu >=1 and nu<=10 :
    if nu==na :
        print("felicidades adivinaste el numero ")
print("el numero ganador era : {}".format(na))
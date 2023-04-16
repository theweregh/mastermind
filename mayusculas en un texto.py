import string
texto_del_usuario = input("ingrese un texto \n")
letras_mayusculas = 0
for letra in texto_del_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1
print("las letras mayusculas son: {}\n".format(letras_mayusculas))


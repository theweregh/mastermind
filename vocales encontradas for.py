vocales = ["a","e","i","o","u"]
frase = "hola hoy estoy aprendiendo python"
vocales_encontradas = 0
for letra in frase:
    if letra in vocales:
        print("he encontrado una "{}"".format(letra))
        vocales_encontradas += 1
print("vocales encontradas: {}".format(vocales_encontradas))
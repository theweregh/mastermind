numero  = int(input("ingrese un numero "))
for number in range(1,11):
    if numero % number == 0:
        print("{}%{} es: par".format(numero,number))
    else:
        print("{}%{} es: impar".format(numero,number))
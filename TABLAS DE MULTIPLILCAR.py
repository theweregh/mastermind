numero = int(input("escriba un numero a multiplicar "))
rango_menor = int(input("escriba el inicio del intervalo "))
rango_mayor = int(input("escriba el final del intervalo "))
for number in range(rango_menor,rango_mayor+1) :
    if number % numero == 0:
       print("el resultado de {}*{} es: {}".format(numero,number,numero * number))
acumulado=int(0)
numero=str("")


while True:
    numero=input("Dame un numero entero: ")
    if numero=="":

        print("Vacio. Salida del programa.")
        break
    else:

        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))

acumulado=int(0)
numero=str("")

#Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición
#(es decir, mientras la condición tenga el valor True).
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
#(Break) ,nos permite salir de adentro de un ciclo (tanto sea for como while ) en medio de su ejecución.
        print("Vacio. Salida del programa.")
        break
    else:

        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))

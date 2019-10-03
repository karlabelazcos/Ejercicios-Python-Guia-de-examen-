numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)

#Un bucle (for) es un bucle que repite el bloque de instrucciones un número prederminado de veces.
#El tipo range es una lista inmutable de números enteros en sucesión aritmética.
#Inmutable significa que, a diferencia de las listas, los range no se pueden modificar.
#Una sucesión artimética es una sucesión en la que la diferencia entre dos términos consecutivos es siempre la misma.
for i in range(1,11):

    salida="{} * {} = {}"
    print(salida.format(numero,i,i*numero))

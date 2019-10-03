#Se utiliza import para elegir un elemento aleatorio de una lista.
import random
#Los numeros con punto decimal es de tipo (float).
numero1=float(10.5)
#La funcion es un conjunto de instrucciones.
#Una definición de función es una sentencia ejecutable.
def miFuncion():

    numero2=float(random.randrange(1,10))
    #Los entre corchetes son para mostrar los resultados.
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

miFuncion()

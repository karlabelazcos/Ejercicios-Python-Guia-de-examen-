#Para convertir este tipo de dato se utiliza (str) que convierte (x) a una cadena.
numero="1234"
#La funcion (type) se utiliza para obtener el tipo de dato de cual objeto.
print(type(numero))
#La cadena se convierte en entero (int).
numero=int(numero)

print(type(numero))
#Pones un (str) y un entre corchetes para poner los valores propocionados (formant).
salida="El numero utilizado es {}"

print(salida.format(numero))

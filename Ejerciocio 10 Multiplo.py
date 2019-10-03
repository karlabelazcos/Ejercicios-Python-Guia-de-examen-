#Se almacena un numero y se convierte en entero.
numero=int(input("Dame un numero: "))

#Una variable booleana es una variable que sólo puede tomar dos posibles valores: True (verdadero) o False (falso).
#Si el residuo es 0 quiere decir que el numero es multiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)

#El AND se usa cuando todas la condiciones son correctas.
#Y el OR se usa cuando solo uno es verdadero la condicion es verdadera.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):

     print("correcto.")
else:
     print("Incorreccto.")

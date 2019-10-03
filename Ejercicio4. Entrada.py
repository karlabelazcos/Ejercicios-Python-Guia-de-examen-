#La función input() permite obtener texto escrito por teclado.
entrada=input()
print(type(entrada))

esEntero=(entrada.isdigit() and entrada.find(".")== -1)
if(esEntero):
#La primera condicion es para comparar si es verdadera.
print("Dato entero. ¡Muy bien!")
#El (else) es como un (SiNo) solo una condicion se debe cumplir.
else:
    #O si es falsa.
    print("Dato no es entero. Intentar nuevamente.")

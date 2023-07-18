#La primera forma, tengo que llamar simpre el archivo
#import Funcion1
#Segunda. forma
from Funcion1 import tablaMultiplicar

print("Te voy a enseñar a multiplicar")
print("Digite que tabla quiere")

valor = int(input())
tablaMultiplicar(valor)


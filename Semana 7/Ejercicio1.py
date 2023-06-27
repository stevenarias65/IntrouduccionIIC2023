#Tipado dinamico
#Fuertemente tipado int edad 
nombre = "Ronald"
edad = 30
peso = 90.3 
activo = True

#Funcion
tipoDatoNombre = type(nombre)
print("El tipo de dato es:",tipoDatoNombre)

nombre = 12
tipoDatoNombre = type(nombre)
print("El tipo de dato es:",tipoDatoNombre)


entrada = input("Digite un dato de entrada: ")
print(type(entrada))

str()
int()
float()
bool()


valor1 = 453
valor2 = 59.058

print("El valor de %5d tiene un precio de %8.2f y el nombre es asd%s" % (valor1,valor2,"Ronald"))

#| Identificador    | Formato           |
#| ----------------:|:-----------------:|
#| %s               | Cadena (string)   |
#| %d               | Entero (integer)  |
#| %o               | Octal             |
#| %x               | Hexadecimal       |
#| %f               | Flotante          |

#356.08977
print(" %10.2f " %(356.08977))


a,b,c,d = 12,"roandl",5.4,"Arias"
print(a)
print(b)
print(c)
print(d)



#Listas o tuplas, Arreglos, Vectores, array
#Tupla se crean dentro de parentesis


miPrimeraLista = [ "Ronald",30,"Docente","Vitara",1.80 ]

print(miPrimeraLista[2])

#Tipo de dato
print(type(miPrimeraLista[1]))

#Mostrar los datos
#len() longitud
#type() tipo dato
#print() mostrar
#input() leer de teclado
print(len(miPrimeraLista))
ultimo = len(miPrimeraLista) - 1

print(miPrimeraLista[len(miPrimeraLista) - 1])
print(miPrimeraLista[0:3])

print(miPrimeraLista)
print(miPrimeraLista[::-1])

miPrimeraLista[0] = "Steven"
print(miPrimeraLista)



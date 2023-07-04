#Eliminar

#remove Elimina por valor
#pop eliminar por indice y devuelve el valor

lista = [1,"hola",5,3,4,5,6]

print("El indice es",lista.index("hola"))

lista.remove(4)
lista.remove(5)
print(lista)
valoreliminado = lista.pop(3)
print("El valor eliminado fue: ", valoreliminado)
print(lista)
print("El indice es",lista.index(6))
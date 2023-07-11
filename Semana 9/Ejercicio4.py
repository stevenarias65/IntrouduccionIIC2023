agenda = [[], []]

cantidadPersonas = int(input("Digite cuantas personas quiere en la agenda: "))

for i in range(cantidadPersonas):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i+1))
    telefono = input("Ingrese el telefono de la persona {}: ".format(i+1))
    agenda[0].append(nombre)
    agenda[1].append(telefono)

print("Informacion de la Agenda")
print("Nombre: ",agenda[0])
print("Telefono: ",agenda[1])





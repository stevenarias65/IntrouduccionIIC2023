agenda = [[], []]

# Obtener los nombres y teléfonos del usuario
nombres = input("Ingrese los nombres separados por espacios: ").split()
telefonos = input("Ingrese los teléfonos separados por espacios: ").split()

# Agregar los nombres y teléfonos a la agenda
agenda[0] = nombres
agenda[1] = telefonos

# Imprimir los datos de la agenda
print("Agenda:")
print("Nombres:", agenda[0])
print("Teléfonos:", agenda[1])
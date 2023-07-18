#Importar librerias
import os 

os.system("clear")
#os.mkdir("Carpeta Creada")
#os.system("cls")
agenda = {}
while True: 
  
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("Dime opción:"))
    if opcion == 1:
        nombre = input("Nombre del contacto:").upper()    
        if nombre in agenda:
            print("%s ya existe su número de teléfono es %s" % (nombre,agenda[nombre]))
            opcion = input("Pulsa 's' si quieres modificar. Otra tecla para continuar.")
            if opcion == "s":
                numero = input("Dame el nuevo número de teléfono:")
                agenda[nombre]=numero
        else:
            numero = input("Dame el número de teléfono:")
            agenda[nombre]=numero
            os.system("clear")
    elif opcion == 2:
        cadena = input("Nombre del contacto a buscar:").upper()    
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                print("El número de teléfono de %s es el %s" % (nombre.title(),agenda[nombre]))
    elif opcion == 3:
        nombre = input("Nombre del contacto para borrar:").upper()    
        if nombre in agenda:
            opcion = input("Pulsa 's' si quieres borrarlo Otra tecla para continuar.")
            if opcion == "s":
                del agenda[nombre]
            os.system("clear")
        else:
            print("No existe el contacto")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre.title(),"->",numero)
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta")
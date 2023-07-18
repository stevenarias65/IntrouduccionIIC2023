#Utilizando Diccionarios me creen una agenda, donde la clave sea el nombre
#Y el valor sea el numero de telefono
#Quiero que pregunte si quiere mas personas 
#Verificar si el nombre ya existe


agenda = {}
 
salir = False
 
while (not salir):
 
    #Pedimos los datos
    nombre=input("Introduce un nombre: ")
    telefono=int(input("Introduce un telefono: "))
  
    #Comprobamos si esta dentro del diccionario
    if(nombre not in agenda):
        #Añadimos el contacto
        agenda[nombre] = telefono
        print('Añadido el contacto')
    else:
        print('El nombre esta repetido')
         
    #Indicamos si queremos salir
    respuesta = input("¿Quieres salir? (S/N)")
 
    if(respuesta == "S"):
        break
 
#Mostramos el diccionario
print(agenda)
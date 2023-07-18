from Funcion3 import login

usuario = input()
contrasenna = input()

validacion,lista,cadena = login(usuario,contrasenna)

print(validacion,lista,cadena)


if validacion:
    print("Login completo")
else:
    print("Error contraseña")
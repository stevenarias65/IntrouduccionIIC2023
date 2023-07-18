def login(usuario,contrasenna):
    validacion = False
    lista = []
    if usuario == "admin" and contrasenna == "adminadmin":
        validacion = True
    else:
        validacion : False
    return bool(validacion),lista,"Hola mundo"


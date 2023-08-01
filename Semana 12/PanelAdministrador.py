from tkinter import *

def ventaAdministrador(usuario,rol):
    ventanaNueva = Tk()

    saludo = "Bienvenido " + usuario
    Label(ventanaNueva,text=saludo).pack()

    if rol == "Administrador":
        Label(ventanaNueva,text="Solo el administrador puede ver").pack()
    


    ventanaNueva.mainloop()
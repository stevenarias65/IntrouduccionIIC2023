from tkinter import *


ventana = Tk()

menuPrincipal = Menu(ventana)
ventana.config(menu=menuPrincipal)

def ventanaSecundaria():
    ventasecundario = Toplevel(menuPrincipal)

inventario = Menu(menuPrincipal)
menuPrincipal.add_cascade(label="Inventario",menu=inventario)
inventario.add_command(label="Agregar al Inventario",command=ventanaSecundaria)
inventario.add_command(label="Ver Inventario")
inventario.add_command(label="eliminar Inventario")
inventario.add_separator()
inventario.add_command(label="Actualizar Invnetario")

compras = Menu(menuPrincipal)
menuPrincipal.add_cascade(label="Compas",menu=compras)
compras.add_command(label="Ver compras")

Salir = Menu(menuPrincipal)
menuPrincipal.add_cascade(label="Salir",menu=Salir)
Salir.add_command(label="Salir",command=ventana.destroy)


ventana.mainloop()



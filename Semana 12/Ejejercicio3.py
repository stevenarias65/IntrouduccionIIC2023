#Importa
import tkinter as tt

ventana = tt.Tk()

ventana.title("Datos personales")
ventana.geometry("200x300")

def cambiarDatos():
    lblCambiar.config(text="Cambiado desde el boton")


btnClick = tt.Button(ventana,text="Darle click",command=cambiarDatos)
btnClick.pack()

lblCambiar = tt.Label(ventana)
lblCambiar.pack() 



ventana.mainloop()
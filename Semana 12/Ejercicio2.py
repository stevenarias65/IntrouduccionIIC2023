#Importa
import tkinter as tt

ventana = tt.Tk()

ventana.title("Datos personales")
ventana.geometry("200x300")

#Widget
#Esta forma es creando la variable
etiqueta1 = tt.Label(ventana,text="Hola mundo, mi primeta etiqueta")
etiqueta1.pack()
etiqueta2 = tt.Label(ventana,text="Hola mundo, mi primeta etiqueta")
etiqueta2.pack()

#Crearlo de forma anonima
tt.Label(ventana,text="Segunda etiqueta").pack()


etiqueta1.config(text="Modifique la etiqueta")


ventana.mainloop()
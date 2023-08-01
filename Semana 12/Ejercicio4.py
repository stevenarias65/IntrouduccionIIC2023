#Importa
import tkinter as tt



def Inicio():
    ventana = tt.Tk()
    ventana.title("Datos personales")
    ventana.geometry("200x300")

    tt.Label(ventana,text="Ingrese los datos",font=("Arial Bold",20)).grid(column=0,row=0)
    global txtDatos
    txtDatos = tt.Entry(ventana)
    txtDatos.grid(column=0,row=1)
    global lblEtiqueta
    lblEtiqueta = tt.Label(ventana)
    lblEtiqueta.grid(column=1,row=1)

    tt.Button(ventana,text="Click Aqui",command=precionar).grid(column=0,row=2)

    ventana.mainloop()

def precionar():
    texto = txtDatos.get()
    lblEtiqueta.config(text=texto)



Inicio()
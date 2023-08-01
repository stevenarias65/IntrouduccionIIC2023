#Importa
import tkinter as tt
from tkinter import ttk
from tkinter import messagebox
from PanelAdministrador import *


def Inicio():
    global ventana
    ventana = tt.Tk()

    ventana.title("Ventana de Inicio")
    ventana.geometry("400x250")
    #ventana.config(width="400",height="500")

    tt.Label(ventana,text="Escoja una opcion",bg="Red",width="100").pack()
    tt.Label(ventana).pack()
    tt.Button(ventana,text="Login",width="30",height="3",bg="Gray",command=Login).pack()
    tt.Label(ventana).pack()
    tt.Button(ventana,text="Registro",width="30",height="3",bg="Gray",command=Registro).pack()

    ventana.mainloop()



def Login():
    ventana_Login = tt.Toplevel(ventana)
    ventana_Login.title("Ventana Login")
    ventana_Login.geometry("300x200")

    tt.Label(ventana_Login,text="Por favor digite los datos").pack()
    global verificarUsuario
    verificarUsuario = tt.StringVar()
    global verificarClave
    verificarClave = tt.StringVar()
    tt.Label(ventana_Login,text="Digite su usuario").pack()
    tt.Entry(ventana_Login,textvariable=verificarUsuario).pack()
    tt.Label(ventana_Login,text="Digite su Calve").pack()
    tt.Entry(ventana_Login,textvariable=verificarClave,show="*").pack()
    tt.Button(ventana_Login,text="Login",command=FuncionVerificarUsuario).pack()


valores = ["Administrador","Usuario","Cajero"]
def Registro():
    ventana_Registro = tt.Toplevel(ventana)
    ventana_Registro.title("Ventana Registro")
    ventana_Registro.geometry("300x200")

    global usuarioRegistro
    global claveRegistro
    global rolRegistro
    usuarioRegistro = tt.StringVar()
    claveRegistro = tt.StringVar()
    rolRegistro = tt.StringVar()
    tt.Label(ventana_Registro,text="Por favor digite usuario").pack()
    entradausuarioRegistro = tt.Entry(ventana_Registro,textvariable=usuarioRegistro).pack()
    tt.Label(ventana_Registro,text="Por favor digite Contraseña").pack()
    entradaclaveRegistro = tt.Entry(ventana_Registro,textvariable=claveRegistro).pack()
    tt.Label(ventana_Registro,text="Por favor elija el rol").pack()
    comboboxRegistro = ttk.Combobox(ventana_Registro,textvariable=rolRegistro,values=valores,state="readonly")
    comboboxRegistro.pack()
    tt.Button(ventana_Registro,text="Guardar",command=GuardarRegistro).pack()


usuario = {}

def GuardarRegistro():
    datos = []
    datos.append(claveRegistro.get())
    datos.append(rolRegistro.get())
    usuario[usuarioRegistro.get()] = datos
    messagebox.showinfo("Alerta","Usuario Guardado")

def FuncionVerificarUsuario():

    encontrar = False
    sesionusuario =""
    sesionrol = ""

    for clave, valor in usuario.items():
        if verificarUsuario.get() == clave and verificarClave.get() == valor[0]:  
            encontrar = True
            sesionusuario = clave
            sesionrol = valor[1]
            break
        else: 
            encontrar = False
    if encontrar:
        messagebox.showinfo("","usuario encontrado")
        ventana.destroy()
        ventaAdministrador(sesionusuario,sesionrol)
        
    else:
        messagebox.showerror("","Error")
        





Inicio()
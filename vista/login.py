import tkinter as tk
from tkinter import *
from tkinter import messagebox
#from Tooltip import Tooltip
import winsound

from controlador.Usuario import Usuario

class Login():

    def verCaracteres(self, event):
        if self.bandera == True:
            self.txtPassword.config(show='*')
            self.btnVer.config(text="ver")
            self.bandera = False
        else:
            self.txtPassword.config(show='')
            self.btnVer.config(text="ocul")
            self.bandera = True

    def validarCampos(self, event):
        if len(self.txtUsuario.get()) > 5 and len(self.txtPassword.get()) > 5:
            if len(self.txtUsuario.get()) <= 25 and len(self.txtPassword.get()) <= 25:
                self.btnIngresar.config(state="normal")
        else:
            self.btnIngresar.config(state="disabled")

        if len(self.txtPassword.get()) > 25:
            self.txtPassword.delete(len(self.txtPassword.get())-1)
        if len(self.txtUsuario.get()) > 25:
            self.txtUsuario.delete(len(self.txtUsuario.get())-1)

    def validarUsuario(self, event):
        caracter = event.keysym
        print(caracter, " fue presionado")
            #if caracter in self.caracteresUsuario or caracter=="BackSpace" or caracter:
        if caracter.isalpha() or caracter == '.' or caracter == "BackSpace":
            self.txtUsuario.config(bg="white", fg="black")
        else:
            self.txtUsuario.config(bg="pink", fg="red")
            # winsound.Beep(1700, 333 )
            
    def ingresar(self, event):
        miUsuario = Usuario()
        miUsuario.iniciarSesion(self.txtUsuario.get(), self.txtPassword.get(), self.ventana)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.config(width=440, height=350)
        self.ventana.title("Inicio de Sesión")

        self.bandera = False
        self.caracteresUsuario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.caracteresPassword = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión")
        self.lblTitulo.place(anchor="center", relx=0.5, y=50)

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(y=125, x=100, width=70, height=25)

        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(x=100, y=200, width=70, height=25)

        self.txtUsuario = tk.Entry(self.ventana)
        self.txtUsuario.place(x=190, y=125, width=150, height=25)
        self.txtUsuario.bind("<KeyRelease>", self.validarCampos)
        self.txtUsuario.bind("<KeyPress>", self.validarCampos)
        self.txtUsuario.bind("<Key>", self.validarUsuario)
        #Tooltip(self.txtUsuario, "Ingrese su nombre de Usuario, solo letras minúsculas.\nmin 5 max 25 caracteres.")
        self.txtPassword = tk.Entry(self.ventana, show='*')
        self.txtPassword.place(y=200, x=190, width=150, height=25)
        self.txtPassword.bind("<KeyRelease>", self.validarCampos)
        self.txtPassword.bind("<KeyPress>", self.validarCampos)

        self.btnAyuda = tk.Button(self.ventana, text="Ayuda")
        self.btnAyuda.place(x=320, y=50)

        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", state="disabled")
        self.btnIngresar.bind("<Button-1>", self.ingresar)
        self.btnIngresar.place(x=140, y=275, width=70, height=25)

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar")
        self.btnLimpiar.place(x=230, y=275, width=70, height=25)

        self.btnVer = tk.Button(self.ventana, text="ver")
        self.btnVer.place(x=360, y=200, width=30, height=25)
        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.verCaracteres)

        self.ventana.mainloop()


Login()

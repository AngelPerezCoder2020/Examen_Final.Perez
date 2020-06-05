import tkinter
from tkinter import *

class vent():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Examen Final")

        self.titulo = Label(ventana, text="BIENVENIDO", font="Arial 12")
        self.titulo.grid(row=0, column=0, columnspan=7)
        
        self.nombre = Label(ventana, text="Nombre")
        self.nombre.grid(row=1, column=1, columnspan=2)

        self.nomb = Entry(ventana)
        self.nomb.focus()
        self.nomb.grid(row=1, column=3, columnspan=3)

        self.apellido = Label(ventana, text="Apellido")
        self.apellido.grid(row=2, column=1, columnspan=2)

        self.apell = Entry(ventana)
        self.apell.grid(row=2, column=3, columnspan=3)

        self.dia = Label(ventana, text="Dia")
        self.dia.grid(row=3, column=1, columnspan=2)

        self.di = Entry(ventana)
        self.di.grid(row=3, column=3, columnspan=3)

        self.mes = Label(ventana, text="Mes")
        self.mes.grid(row=4, column=1, columnspan=2)

        self.me = Entry(ventana)
        self.me.grid(row=4, column=3, columnspan=3)

        self.año = Label(ventana, text="Año")
        self.año.grid(row=5, column=1, columnspan=2)

        self.añ = Entry(ventana)
        self.añ.grid(row=5, column=3, columnspan=3)

        self.F1 = Button(ventana, text="Función 1")
        self.F1.grid(row=6, column=1)

        self.F2 = Button(ventana, text="Función 2")
        self.F2.grid(row=6, column=2)

        self.F3 = Button(ventana, text="Función 3")
        self.F3.grid(row=6, column=3)

        self.F4 = Button(ventana, text="Función 4")
        self.F4.grid(row=6, column=4)

        self.F5 = Button(ventana, text="Función 5")
        self.F5.grid(row=6, column=5)

        self.respuest = Label(ventana, Text="Aqui aparecerán los resultados")
        self.respuest.grid(row=6, column=0, columnspan=7)


ventana = Tk()
general = vent(ventana)
ventana.mainloop()
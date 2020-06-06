from tkinter import Tk, Frame, Label, Entry, Button
import datetime
from datetime import date

class vent():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Examen Final")

        self.frame = Frame(ventana)
        self.frame.grid(row=0, column=0, padx = 40, ipady = 10)

        self.titulo = Label(self.frame, text="BIENVENIDO", font="Arial 16")
        self.titulo.grid(row=0, column=0, columnspan=6)
        
        self.nombre = Label(self.frame, text="Nombre")
        self.nombre.grid(row=1, column=0, columnspan=2)

        self.name = Entry(self.frame, width=30)
        self.name.grid(row=1, column=2, columnspan=3)
        self.name.focus()

        self.apellido = Label(self.frame, text="Apellido")
        self.apellido.grid(row=2, column=0,columnspan=2)

        self.ape = Entry(self.frame, width=30)
        self.ape.grid(row=2, column=2, columnspan=3)

        self.dia = Label(self.frame, text="Dia")
        self.dia.grid(row=3, column=0,columnspan=2)

        self.day = Entry(self.frame, width=30)
        self.day.grid(row=3, column=2, columnspan=3)

        self.mes = Label(self.frame, text="Mes")
        self.mes.grid(row=4, column=0,columnspan=2)

        self.month = Entry(self.frame, width=30)
        self.month.grid(row=4, column=2, columnspan=3)

        self.año = Label(self.frame, text="Año")
        self.año.grid(row=5, column=0,columnspan=2)

        self.year = Entry(self.frame, width=30)
        self.year.grid(row=5, column=2, columnspan=3)

        def binarios(num):

            lista = []
            while num >= 1:
                lista.insert(0,num%2)
                num = num // 2
                binario = "".join(str(i) for i in lista)

            return binario  

        def fecha_binarios():
            año = int(self.year.get())
            mes = int(self.month.get())
            dia = int(self.day.get())

            baño = binarios(año)
            bimes = binarios(mes)
            bidia = binarios(dia)

            self.respuest["text"] = f"{año}/{mes}/{dia}  = {baño}/{bimes}/{bidia}"

        self.F1 = Button(self.frame, text="Función 1", command = fecha_binarios)
        self.F1.grid(row=6, column=0)

        def vivido():
            hoy = datetime.datetime.now()
            a = int(hoy.year)
            m = int(hoy.month)
            d = int(hoy.day)
            hoy2 = date(a,m,d)

            año = int(self.year.get())
            mes = int(self.month.get())
            dia = int(self.day.get())

            nacimiento = date(año,mes,dia)

            dias = hoy2 - nacimiento

            dias2 = dias.days

            self.respuest["text"] = f"Usted nació el {nacimiento} y ah vivido {dias2} dias"
         
        self.F2 = Button(self.frame, text="Función 2", command = vivido)
        self.F2.grid(row=6, column=1)

        def parinpar():
            nombre = f"{self.name.get()}"
            apellido = f"{self.ape.get()}"

            conteoNo = len(nombre)
            conteoAp = len(apellido)

            if conteoNo % 2 == 0:
                n = "su nombre es par"
            else:
                n = "su nombre es impar"

            if conteoAp % 2 == 0:
                m = "su apellido es par"
            else:
                m = "su apellido es impar"

            respuesta = f"{nombre} {apellido} {n} y {m}"

            self.respuest["text"] = respuesta

        self.F3 = Button(self.frame, text="Función 3", command=parinpar)
        self.F3.grid(row=6, column=2)

        def vocal(texto):
            vocales = "aeiouAEIOU"

            return [v for v in texto if v in vocales]

        def v_c():
            nombre = f"{self.name.get()} {self.ape.get()}"
            cantT = int(len(nombre))
            cantv = int(len(vocal(nombre)))
            cantc = (cantT - cantv)-1

            self.respuest["text"] = f"{nombre} tiene {cantv} vocales y {cantc} consonantes"
            
        self.F4 = Button(self.frame, text="Función 4", command= v_c)
        self.F4.grid(row=6, column=3)

        def alrevez():
            nombre = self.name.get()
            apellido = self.ape.get()

            nombrea = nombre[::-1]
            apellidoa = apellido[::-1]

            self.respuest["text"] = f"{nombre} {apellido} al revés {apellidoa} {nombrea}"

        self.F5 = Button(self.frame, text="Función 5", command = alrevez)
        self.F5.grid(row=6, column=4)

        self.respuest = Label(self.frame, text="Acá se verá el resultado de las funciones")
        self.respuest.grid(row=7, column=0, columnspan=6)


ventana = Tk()
general = vent(ventana)
ventana.mainloop()
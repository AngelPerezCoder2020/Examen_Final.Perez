import tkinter
from tkinter import *

class vent():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Proyecto_Final_Perez.Damas")
        

ventana = Tk()
general = vent(ventana)
ventana.mainloop()
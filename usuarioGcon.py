from tkinter import *


class InitialPrm():
    
    CUav = 0
    
    def __init__(self, ventana):
        
        self.lab_usu_Encabezado = Label(ventana, text = 'gestion usuarios')
        self.lab_usu_Encabezado.place(relx = 0.2, rely = 0.03)
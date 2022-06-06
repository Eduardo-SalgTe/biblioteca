import tkinter

import lobby as lob
import guc
import gum
import gur

class InitialPrm():
    
    CUav = 0
    
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('Gestion Usuarios')
        self.center_window(ventana, 900, 550)
        
        
        self.lab_usu_ci = tkinter.Button(ventana, text = 'Consultar informacion', command = lambda : self.ci(ventana))
        self.lab_usu_mi = tkinter.Button(ventana, text = 'Modificar informacion', command = lambda : self.mi(ventana))
        self.lab_usu_ru = tkinter.Button(ventana, text = 'Registrar usuario', command = lambda : self.ru(ventana))
        self.lab_usu_eu = tkinter.Button(ventana, text = 'Eliminar usuario')
        self.lab_usu_mp = tkinter.Button(ventana, text = 'Menu principal', command = lambda : self.ret(ventana))
        
        self.lab_usu_ci.place(relx = 0.2, rely = 0.1)
        self.lab_usu_mi.place(relx = 0.2, rely = 0.15)
        self.lab_usu_ru.place(relx = 0.2, rely = 0.2)
        self.lab_usu_eu.place(relx = 0.2, rely = 0.25)
        self.lab_usu_mp.place(relx = 0.2, rely = 0.6)
        
        ventana.mainloop()
        
    def ci(self, vent):
        vent.destroy()
        guc.InitialParamt()
        
    def mi(self, vent):
        vent.destroy()
        gum.InitialParamt()
    
    def ru(self, vent):
        vent.destroy()
        gur.InitialParamt()
        
    def eu(self, vent):
        vent.destroy()
        
    def ret(self, vent):
        vent.destroy()
        lob.Lobby()
    def center_window(self, vent,  width=300, height=200):
        # get screen width and height
        screen_width = vent.winfo_screenwidth()
        screen_height = vent.winfo_screenheight()
    
        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        vent.geometry('%dx%d+%d+%d' % (width, height, x, y))
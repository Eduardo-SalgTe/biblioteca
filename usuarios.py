import tkinter
import time 

import lobby as lob
import database as db

class InitialParm():
    
    CUav = 0
    
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('Control Usuarios')
        self.center_window(ventana, 900, 550)
        
        self.lab_usu_reg = tkinter.Label(ventana, text = 'registro:')
        self.lab_usu_cb = tkinter.Label(ventana, text = 'codigo:')
        self.lab_usu_nom = tkinter.Label(ventana, text = 'nombre:')
        self.lab_usu_fchIn = tkinter.Label(ventana, text = 'fecha ingreso:')
        self.lab_usu_hrIn = tkinter.Label(ventana, text = 'hora entrada:')
        self.lab_usu_hrOu = tkinter.Label(ventana, text = 'hora salida:')
        self.lab_usu_mat = tkinter.Label(ventana, text = 'material prestado:')
        
        
        self.ent_usu_reg = tkinter.Entry(ventana, width = 20)
        self.ent_usu_cb = tkinter.Entry(ventana, width = 20)
        self.ent_usu_nom = tkinter.Entry(ventana, width = 20)
        self.ent_usu_fchIn = tkinter.Entry(ventana, width = 20)
        self.ent_usu_hrIn = tkinter.Entry(ventana, width = 20)
        self.ent_usu_hrOu = tkinter.Entry(ventana, width = 20)
        self.ent_usu_mat = tkinter.Entry(ventana, width = 20)
        
        self.butt_usu_ver = tkinter.Button(ventana, text = 'ver usuario', command = lambda : self.verUsu(ventana))
        self.butt_usu_return = tkinter.Button(ventana, text = 'menu principal', command = lambda : self.menuPr(ventana))
        
        self.butt_usu_ver.place(relx = 0.03, rely = 0.6)
        self.butt_usu_return.place(relx = 0.8, rely = 0.6)

        self.lab_usu_reg.place(relx = 0.1, rely = 0.1)
        self.lab_usu_cb.place(relx = 0.1, rely = 0.15)
        self.lab_usu_nom.place(relx = 0.1, rely = 0.2)
        self.lab_usu_fchIn.place(relx = 0.1, rely = 0.25)
        self.lab_usu_hrIn.place(relx = 0.1, rely = 0.3)
        self.lab_usu_hrOu.place(relx = 0.1, rely = 0.35)
        self.lab_usu_mat.place(relx = 0.1, rely = 0.4)
        
        self.ent_usu_reg.place(relx = 0.5, rely = 0.1)
        self.ent_usu_cb.place(relx = 0.5, rely = 0.15)
        self.ent_usu_nom.place(relx = 0.5, rely = 0.2)
        self.ent_usu_fchIn.place(relx = 0.5, rely = 0.25)
        self.ent_usu_hrIn.place(relx = 0.5, rely = 0.3)
        self.ent_usu_hrOu.place(relx = 0.5, rely = 0.35)
        self.ent_usu_mat.place(relx = 0.5, rely = 0.4)
        
        ventana.mainloop()
        
    
    
    def verUsu(self, vent):
        self.CUav = 1
        vent.destroy()
        
        
    def menuPr(self, vent):
        self.CUav = 2
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
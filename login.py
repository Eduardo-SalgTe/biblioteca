import tkinter
from tkinter.messagebox import _show
import database as db

import lobby as lob

class Logeo():
    
    Tpass = 'sate007'
    avanza = 0
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('INICIO DE SESION')
        self.center_window(ventana, 900, 550)
        #ventana.eval('tk::PlaceWindow . center')
        #ventana.geometry('900x600')
        
        self.lab_log_user = tkinter.Label(ventana, text = 'Ingresar usuario')
        self.lab_log_pass = tkinter.Label(ventana, text = 'Ingresar contrasena')
        self.lab_log_user.place(relx = 0.1, rely = 0.1)
        self.lab_log_pass.place(relx = 0.1, rely = 0.2)
    
        self.ent_log_user = tkinter.Entry(ventana, width = 15)
        self.ent_log_pass = tkinter.Entry(ventana, width = 15)
        self.ent_log_user.place(relx = 0.1, rely = 0.125)
        self.ent_log_pass.place(relx = 0.1, rely = 0.225)
        
        self.but_log_acces = tkinter.Button(ventana, text = 'Iniciar Sesion', command = lambda : self.Next(ventana, self.ent_log_pass, self.ent_log_user))
        self.but_log_acces.place(relx = 0.25, rely = 0.28)
        
        ventana.mainloop()
        
    def parametros(self):
        return 0
    
    def validacion(self, entrypass, entrynam):
        usr = entrynam.get()
        cadpass = entrypass.get()
        
        synt = "SELECT tipo_cuenta FROM gur WHERE contrasena = '{0}'"
        synt2 = "SELECT nombre FROM gur WHERE nombre = '{0}' AND tipo_cuenta = 'admin'"
        db1 = db.DataBase()
        txt = db1.selectONE(cadpass, synt)
        txt2 = db1.selectONE(usr, synt2)
        if(txt != "" and txt2 != ""):
            db1.close()
            self.avanza = 1
        elif(txt2 == ""):
            db1.close()
            _show('error', 'verifica usuario')
        elif(txt == '' and txt2 != ''):
            db1.close()
            _show('error', 'verifica contrasena')
        
    def Next(self, vent, entrypass, entrynam):
        usr = entrynam.get()
        self.validacion(entrypass, entrynam)
        if self.avanza == 1:
            vent.destroy()
            lob.Lobby()
            #camara.CamaraRun()
            
    def center_window(self, vent,  width=300, height=200):
        # get screen width and height
        screen_width = vent.winfo_screenwidth()
        screen_height = vent.winfo_screenheight()
    
        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        vent.geometry('%dx%d+%d+%d' % (width, height, x, y))  
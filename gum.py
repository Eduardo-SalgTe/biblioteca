import tkinter
from tkinter import END

import database as db
import usuariosGst as ret
import barcode as bc

class InitialParamt():
    matr = []
    cadenaCurp = ''
    def __init__(self):
        
        ventana = tkinter.Tk()
        ventana.title('Gestion usuarios - Modificar')
        self.center_window(ventana, 900, 550)
        
        lab_gum_nomb1 = tkinter.Label(ventana, text = 'buscar por nombre:')
        lab_gum_curp = tkinter.Label(ventana, text = 'buscar por curp:')
        lab_gum_nomb2 = tkinter.Label(ventana, text = 'nombre:')
        lab_gum_ape = tkinter.Label(ventana, text = 'apellidos:')
        lab_gum_edad = tkinter.Label(ventana, text = 'edad:')
        lab_gum_loc = tkinter.Label(ventana, text = 'localidad:')
        lab_gum_est = tkinter.Label(ventana, text = 'educacion:')
        lab_gum_tel = tkinter.Label(ventana, text = 'telefono:')
        
        butt_gum_cb = tkinter.Button(ventana, text = 'buscar por codigo de barras', command = lambda : self.decode())
        butt_gum_go = tkinter.Button(ventana, text = 'consultar', command = lambda : self.consult())
        butt_gum_ret = tkinter.Button(ventana, text = 'regresar', command = lambda : self.retorno(ventana))
        butt_gum_apl = tkinter.Button(ventana, text = 'aplicar')
        
        self.ent_gum_nom = tkinter.Entry(ventana, width = 20)
        self.ent_gum_app = tkinter.Entry(ventana, width = 20)
        self.ent_gum_edad = tkinter.Entry(ventana, width = 20)
        self.ent_gum_loc = tkinter.Entry(ventana, width = 20)
        self.ent_gum_edu = tkinter.Entry(ventana, width = 20)
        self.ent_gum_tel = tkinter.Entry(ventana, width = 20)
        
        self.ent_gum_snom = tkinter.Entry(ventana, width = 20)
        self.ent_gum_scrp = tkinter.Entry(ventana, width = 20)
        self.ent_gum_snom.place(relx = 0.2, rely = 0.1)
        self.ent_gum_scrp.place(relx = 0.2, rely = 0.15)
        
        self.ent_gum_nom.place(relx = 0.35, rely = 0.35)
        self.ent_gum_app.place(relx = 0.35, rely = 0.4)
        self.ent_gum_edad.place(relx = 0.35, rely = 0.45)
        self.ent_gum_loc.place(relx = 0.35, rely = 0.5)
        self.ent_gum_edu.place(relx = 0.35, rely = 0.55)
        self.ent_gum_tel.place(relx = 0.35, rely = 0.6)
        
        
        lab_gum_nomb1.place(relx = 0.1, rely = 0.1, anchor = 'e')
        lab_gum_curp.place(relx = 0.1, rely = 0.15, anchor = 'e')
        lab_gum_nomb2.place(relx = 0.3, rely = 0.35, anchor = 'e')
        lab_gum_ape.place(relx = 0.3, rely = 0.4, anchor = 'e')
        lab_gum_edad.place(relx = 0.3, rely = 0.45, anchor = 'e')
        lab_gum_loc.place(relx = 0.3, rely = 0.5, anchor = 'e')
        lab_gum_est.place(relx = 0.3, rely = 0.55, anchor = 'e')
        lab_gum_tel.place(relx = 0.3, rely = 0.6, anchor = 'e')

        butt_gum_cb.place(relx = 0.1, rely = 0.2)
        butt_gum_go.place(relx = 0.3, rely = 0.2)
        butt_gum_ret.place(relx = 0.5, rely = 0.65)
        butt_gum_apl.place(relx = 0.5, rely = 0.7)
        
        ventana.mainloop()
        
    def consult(self):
        cadd = self.ent_gum_scrp.get()
        if cadd != '':
            sintax = "SELECT nombre, apellidoP, apellidoM, edad, localidad, curp,telefono FROM gur WHERE curp = '{0}'"
            dt = db.DataBase()
            dt.select(cadd, sintax)
            self.matr = dt.mat
            dt.close()
            print('matriz ->', self.matr)
            
            self.ent_gum_nom.insert(END, self.matr[0])
            self.ent_gum_app.insert(END, (self.matr[1], self.matr[2]))
            self.ent_gum_edad.insert(END, self.matr[3])
            self.ent_gum_loc.insert(END, self.matr[4])
            self.ent_gum_edu.insert(END, self.matr[5])
            self.ent_gum_tel.insert(END, self.matr[6])
    
        
    def decode(self):
        stt = bc.Decodificador()
        self.cadenaCurp = stt.curpp
        
        self.ent_gum_scrp.insert(END, self.cadenaCurp)
    
    def retorno(self, vent):
        vent.destroy()
        ret.InitialPrm()
    def center_window(self, vent,  width=300, height=200):
        # get screen width and height
        screen_width = vent.winfo_screenwidth()
        screen_height = vent.winfo_screenheight()
    
        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        vent.geometry('%dx%d+%d+%d' % (width, height, x, y))
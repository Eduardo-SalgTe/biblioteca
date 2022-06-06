import tkinter
from tkinter.messagebox import _show

import database
import usuariosGst as ret

class InitialParamt():
    
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('Gestion usuarios - Registrar')
        self.center_window(ventana, 900, 550)
        
        self.lab_gur_nom = tkinter.Label(ventana, text = 'nombre:')
        self.lab_gur_apP = tkinter.Label(ventana, text = 'apellido Paterno:')
        self.lab_gur_apM = tkinter.Label(ventana, text = 'apellido Materno:')
        self.lab_gur_edad = tkinter.Label(ventana, text = 'edad:')
        self.lab_gur_curp = tkinter.Label(ventana, text = 'curp:')
        self.lab_gur_loc = tkinter.Label(ventana, text = 'localidad:')
        self.lab_gur_dir = tkinter.Label(ventana, text = 'direccion:')
        self.lab_gur_tel = tkinter.Label(ventana, text = 'telefono:')
        self.lab_gur_mail = tkinter.Label(ventana, text = 'correo electronico:')
        self.lab_gur_tipo = tkinter.Label(ventana, text = 'tipo(cuenta):')
        self.lab_gur_pass = tkinter.Label(ventana, text = 'contrasena:')
        self.lab_gur_rpass = tkinter.Label(ventana, text = 'rep contrasena:')
        
        self.ent_gur_nom = tkinter.Entry(ventana, width = 20)
        self.ent_gur_apP = tkinter.Entry(ventana, width = 20)
        self.ent_gur_apM = tkinter.Entry(ventana, width = 20)
        self.ent_gur_edad = tkinter.Entry(ventana, width = 20)
        self.ent_gur_curp = tkinter.Entry(ventana, width = 20)
        self.ent_gur_loc = tkinter.Entry(ventana, width = 20)
        self.ent_gur_dir = tkinter.Entry(ventana, width = 20)
        self.ent_gur_tel = tkinter.Entry(ventana, width = 20)
        self.ent_gur_mail = tkinter.Entry(ventana, width = 20)
        self.ent_gur_tipo = tkinter.Entry(ventana, width = 20)
        self.ent_gur_pass = tkinter.Entry(ventana, width = 20)
        self.ent_gur_rpass = tkinter.Entry(ventana, width = 20)
        
        self.butt_gur_cle = tkinter.Button(ventana, text = 'limpiar campos')
        self.butt_gur_ret = tkinter.Button(ventana, text = 'regresar', command = lambda : self.retorno(ventana))
        self.butt_gur_reg = tkinter.Button(ventana, text = 'registrar', command  = lambda : self.cargar())
        self.butt_gur_pic = tkinter.Button(ventana, text = 'tomar/cargar\nfotografia')
        
        self.lab_gur_nom.place(relx = 0.13, rely = 0.1, anchor = 'e')
        self.lab_gur_apP.place(relx = 0.13, rely = 0.15, anchor = 'e')
        self.lab_gur_apM.place(relx = 0.13, rely = 0.2, anchor = 'e')
        self.lab_gur_edad.place(relx = 0.13, rely = 0.25, anchor = 'e')
        self.lab_gur_curp.place(relx = 0.13, rely = 0.3, anchor = 'e')
        self.lab_gur_loc.place(relx = 0.13, rely = 0.35, anchor = 'e')
        self.lab_gur_dir.place(relx = 0.13, rely = 0.4, anchor = 'e')
        self.lab_gur_tel.place(relx = 0.13, rely = 0.45, anchor = 'e')
        self.lab_gur_mail.place(relx = 0.13, rely = 0.5, anchor = 'e')
        self.lab_gur_tipo.place(relx = 0.13, rely = 0.55, anchor = 'e')
        self.lab_gur_pass.place(relx = 0.13, rely = 0.6, anchor = 'e')
        self.lab_gur_rpass.place(relx = 0.13, rely = 0.65, anchor = 'e')
        
        self.ent_gur_nom.place(relx = 0.13, rely = 0.1)
        self.ent_gur_apP.place(relx = 0.13, rely = 0.15)
        self.ent_gur_apM.place(relx = 0.13, rely = 0.2)
        self.ent_gur_edad.place(relx = 0.13, rely = 0.25)
        self.ent_gur_curp.place(relx = 0.13, rely = 0.3)
        self.ent_gur_loc.place(relx = 0.13, rely = 0.35)
        self.ent_gur_dir.place(relx = 0.13, rely = 0.4)
        self.ent_gur_tel.place(relx = 0.13, rely = 0.45)
        self.ent_gur_mail.place(relx = 0.13, rely = 0.5)
        self.ent_gur_tipo.place(relx = 0.13, rely = 0.55)
        self.ent_gur_pass.place(relx = 0.13, rely = 0.6)
        self.ent_gur_rpass.place(relx = 0.13, rely = 0.65)
        
        
        self.butt_gur_cle.place(relx = 0.13, rely = 0.7)
        self.butt_gur_ret.place(relx = 0.33, rely = 0.7)
        self.butt_gur_pic.place(relx = 0.7, rely = 0.3)
        self.butt_gur_reg.place(relx = 0.7, rely = 0.36)
        
        ventana.mainloop()
    
    def cargar(self): 
        mat = ['','','',0,'','','',0,'','','','']
        ma2t = ['','','',0,'','','',0,'','','','']
        mat[0] = self.ent_gur_nom.get()
        mat[1] = self.ent_gur_apP.get()
        mat[2] = self.ent_gur_apM.get()
        mat[3] = self.ent_gur_edad.get()
        mat[4] = self.ent_gur_curp.get()
        mat[5] = self.ent_gur_loc.get()
        mat[6] = self.ent_gur_dir.get()
        mat[7] = self.ent_gur_tel.get()
        mat[8] = self.ent_gur_mail.get()
        mat[9] = self.ent_gur_tipo.get()
        mat[10] = self.ent_gur_pass.get()
        mat[11] = self.ent_gur_rpass.get()
        print('masat', mat)
        co = 0
        for c in range(len(mat)):
            if mat[c] == ma2t[c]:
                co += 1
        
        if (co < 1):
            print('son diferentes')
            db = database.DataBase()
            db.inssert(mat)
            db.close()
        else:
            _show('error', 'debes llenar los parametros')
        
    def retorno(self, vent):
        print('fasdfadf')
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
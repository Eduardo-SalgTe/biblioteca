import tkinter

import lobby as lob
import la
import lm
import le

class InitialPrm():
    
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('Gestion Libros')
        #ventana.eval('tk::PlaceWindow . center')
        #ventana.geometry('900x600')
        self.center_window(ventana, 900, 600)
        
        self.butt_lbg_agr = tkinter.Button(ventana, text = 'agregar libro', command = lambda : self.al(ventana))
        self.butt_lbg_mod = tkinter.Button(ventana, text = 'modificar libro', command = lambda : self.ml(ventana))
        self.butt_lbg_del = tkinter.Button(ventana, text = 'eliminar libro', command = lambda : self.el(ventana))
        self.butt_lbg_ret = tkinter.Button(ventana, text = 'regresar', command = lambda : self.retorno(ventana))
                
        self.butt_lbg_agr.place(relx = 0.2, rely = 0.1)
        self.butt_lbg_mod.place(relx = 0.2, rely = 0.15)
        self.butt_lbg_del.place(relx = 0.2, rely = 0.2)
        self.butt_lbg_ret.place(relx = 0.2, rely = 0.3)
        
        ventana.mainloop()
        
    def al(self, vent):
        vent.destroy()
        la.InitialParamt()
    
    def ml(self, vent):
        vent.destroy()
        lm.InitialParamt()
        
    def el(self, vent):
        vent.destroy()
        le.InitialParamt()
        
    def retorno(self, vent):
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
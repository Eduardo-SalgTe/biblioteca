import tkinter

import librosGst as ret

class InitialParamt():
    
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('Libros - Eliminar')
        self.center_window(ventana, 900, 550)
        
        self.lab_le_sea = tkinter.Label(ventana, text = 'buscar por ISBN:')
        self.lab_le_lib = tkinter.Label(ventana, text = 'libro:')
        self.lab_le_aut = tkinter.Label(ventana, text = 'autor:')
        self.lab_le_isb = tkinter.Label(ventana, text = 'ISBN:')
        self.lab_le_dis = tkinter.Label(ventana, text = 'disponibles:')
        self.lab_le_pre = tkinter.Label(ventana, text = 'prestados:')
        
        self.butt_le_isb = tkinter.Button(ventana, text = 'buscar por codigo\n  de barras')
        self.butt_le_sea = tkinter.Button(ventana, text = 'buscar')
        self.butt_le_eli = tkinter.Button(ventana, text = 'eliminar')
        self.butt_le_ret = tkinter.Button(ventana, text = 'regresar')
        
        self.butt_le_isb.place(relx = 0.1, rely = 0.05)
        self.lab_le_sea.place(relx = 0.1, rely = 0.15)
        self.butt_le_sea.place(relx = 0.3, rely = 0.15)
        
        self.lab_le_lib.place(relx = 0.1, rely = 0.2)
        self.lab_le_aut.place(relx = 0.1, rely = 0.25)
        self.lab_le_isb.place(relx = 0.1, rely = 0.3)
        self.lab_le_dis.place(relx = 0.1, rely = 0.35)
        self.lab_le_pre.place(relx = 0.1, rely = 0.4)
        
        self.butt_le_eli.place(relx = 0.3, rely = 0.4)
        self.butt_le_ret.place(relx = 0.2, rely = 0.45)
        
        ventana.mainloop()
        
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
import tkinter

import lobby as lob

class InitialPrm():
    
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('Control Libros')
        self.center_window(ventana, 900, 550)
        
        self.lab_lib_sea = tkinter.Label(ventana, text = 'buscar por ISBN:')
        self.lab_lib_pre = tkinter.Label(ventana, text = 'libro:')
        self.lab_lib_lib = tkinter.Label(ventana, text = 'autor:')
        self.lab_lib_aut = tkinter.Label(ventana, text = 'ISBN:')
        self.lab_lib_isb = tkinter.Label(ventana, text = 'disponibles:')
        self.lab_lib_dis = tkinter.Label(ventana, text = 'prestados:')
        
        self.butt_lib_cb = tkinter.Button(ventana, text = 'buscar por codigo\n  de barras')
        self.butt_lib_sea = tkinter.Button(ventana, text = 'buscar')
        self.butt_lib_con = tkinter.Button(ventana, text = 'consultar\ninformacion')
        self.butt_lib_ret = tkinter.Button(ventana, text = 'menu principal', command = lambda : self.retorno(ventana))
        
        
        self.butt_lib_cb.place(relx = 0.1, rely = 0.1)
        self.lab_lib_sea.place(relx = 0.1, rely = 0.17)
        self.butt_lib_sea.place(relx = 0.5, rely = 0.17)
        
        self.lab_lib_lib.place(relx = 0.1, rely = 0.25)
        self.lab_lib_aut.place(relx = 0.1, rely = 0.3)
        self.lab_lib_isb.place(relx = 0.1, rely = 0.35)
        self.lab_lib_dis.place(relx = 0.1, rely = 0.4)
        self.lab_lib_pre.place(relx = 0.1, rely = 0.45)
        
        self.butt_lib_con.place(relx = 0.5, rely = 0.38)
        self.butt_lib_ret.place(relx = 0.25, rely = 0.55)
        
        ventana.mainloop()
    
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
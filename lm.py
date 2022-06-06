import tkinter

import librosGst as ret

class InitialParamt():
    def __init__(self):
        ventana = tkinter.Tk()
        ventana.title('Libros - Modificar')
        self.center_window(ventana, 900, 550)
        
        self.lab_la_isbn = tkinter.Label(ventana, text = 'ISBN:')
        self.lab_la_tit = tkinter.Label(ventana, text = 'titulo:')
        self.lab_la_aut = tkinter.Label(ventana, text = 'autor:')
        self.lab_la_edi = tkinter.Label(ventana, text = 'editorial:')
        self.lab_la_frg = tkinter.Label(ventana, text = 'fecha registro:')
        self.lab_la_can = tkinter.Label(ventana, text = 'cantidad:')
        
        self.butt_la_agr = tkinter.Button(ventana, text = 'modificar')
        self.butt_la_ret = tkinter.Button(ventana, text = 'regresar', command = lambda : self.retorno(ventana))
        
        self.lab_la_isbn.place(relx = 0.1, rely = 0.1)
        self.lab_la_tit.place(relx = 0.1, rely = 0.15)
        self.lab_la_aut.place(relx = 0.1, rely = 0.2)
        self.lab_la_edi.place(relx = 0.1, rely = 0.25)
        self.lab_la_frg.place(relx = 0.1, rely = 0.3)
        self.lab_la_can.place(relx = 0.1, rely = 0.35)
        
        self.butt_la_agr.place(relx = 0.4, rely = 0.2)
        self.butt_la_ret.place(relx = 0.2, rely = 0.4)
        
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
import tkinter

import usuarios as user
import usuariosGst as userG
import libros as lib
import librosGst as libG

class Lobby():
    
    matBut = [0, 0, 0, 0]
    
    def __init__(self):
        
        ejex = 0.1
        ejey = 0.35
        
        ventana = tkinter.Tk()
        ventana.title('MENU PRINCIPAL')
        self.center_window(ventana, 900, 550)
        #ventana.eval('tk::PlaceWindow . center')
        #ventana.geometry('900x600')
        self.lob_butt_UC = tkinter.Button(ventana, text = 'control usuarios', command = lambda : self.UC(ventana))
        self.lob_butt_UG = tkinter.Button(ventana, text = 'gestion usuarios', command = lambda : self.UG(ventana))
        self.lob_butt_LC = tkinter.Button(ventana, text = 'control libros', command = lambda : self.LC(ventana))
        self.lob_butt_LG = tkinter.Button(ventana, text = 'gestion libros', command = lambda : self.LG(ventana))
        
        self.lob_butt_Cl = tkinter.Button(ventana, text = 'Cerrar', command = lambda : self.closeWin(ventana))
        
        self.lob_butt_UC.place(relx = ejex, rely = ejey)
        ejex += 0.20
        self.lob_butt_UG.place(relx = ejex, rely = ejey)
        ejex += 0.20
        self.lob_butt_LC.place(relx = ejex, rely = ejey)
        ejex += 0.20
        self.lob_butt_LG.place(relx = ejex, rely = ejey)
        ejex += 0.20
        
        self.lob_butt_Cl.place(relx = 0, rely = 0)
        
        ventana.mainloop()
    def UC (self, vent):
        self.matBut[0] = 1
        self.closeWin(vent)
        user.InitialParm()
        
        
    def UG (self, vent):
        self.matBut[1] = 1
        self.closeWin(vent)
        userG.InitialPrm()
    
    def LC (self, vent):
        self.matBut[2] = 1
        self.closeWin(vent)
        lib.InitialPrm()
        
    def LG (self, vent):
        self.matBut[3] = 1
        self.closeWin(vent)
        libG.InitialPrm()
    
    def closeWin(self, vent):
        vent.destroy()
        
    def center_window(self, vent,  width=300, height=200):
        # get screen width and height
        screen_width = vent.winfo_screenwidth()
        screen_height = vent.winfo_screenheight()
    
        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        vent.geometry('%dx%d+%d+%d' % (width, height, x, y))
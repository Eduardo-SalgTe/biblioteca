import tkinter

import barcode as bc
import lobby as lb

from pygments.lexers._vim_builtins import command
class CamaraRun():
    cadenaCurp = ""
    
    def __init__(self):
        
        ventana = tkinter.Tk()
        ventana.title('CAMARA')
        ventana.geometry('200x150')
       

        butt_guc_cb = tkinter.Button(ventana, text = 'ACTIVAR CAMARA', command = lambda : self.decode())
        butt_guc_rt = tkinter.Button(ventana, text = 'REGRESAR', command = lambda : self.returN())
        butt_guc_cb.place(relx = 0.15, rely = 0.1)
        butt_guc_rt.place(relx = 0.3, rely = 0.3)
        
        ventana.mainloop()
        
    def decode(self):
        stt = bc.Decodificador()
        self.cadenaCurp = stt.curpp
        print(self.cadenaCurp)
        
    def returN(self):
        lb.Lobby()
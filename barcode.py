import cv2
import numpy as np
from pyzbar.pyzbar import decode
from tkinter.messagebox import _show
import database as db

class Decodificador():
    curpp = ''
    bool = True
    def __init__(self):
        cap = cv2.VideoCapture(1)
        #amcho de camara
        cap.set(3, 640)
        #altp de camara
        cap.set(4, 480)
        
        sintax = "SELECT curp FROM gur WHERE curp = '{0}'"
        
        with open('curp.txt') as f:
            #se guardan las lineas de texto en un arreglo
            mydatalist = f.read().splitlines()
        db1 = db.DataBase()
        while(self.bool):
            #se guarda imagen de camara
            success,img = cap.read()
            #detectar >codigos< en la imagen
            for barcode in decode(img):
                #decodificar codigo barcode
                mydata = barcode.data.decode('utf-8')
                #imprimir >codigo(s)<
                #print(mydata)
                
                ent = db1.selectONE(mydata, sintax)
                #si codigo esta en arreglo
                if mydata == ent:
                    myoutput = 'EXISTE'
                    color = (0, 255, 0)
                    self.curpp = mydata
                    self.bool = False
                #si codigo no esta en arreglo
                else:
                    myoutput = 'NO EXISTE'
                    color = (0, 0, 255)
                    #self.curpp = myoutput
                    self.bool = False
                    #_show('error', 'no existe usuario')
                
                #coordenadas de barcode/codigo
                pts = np.array([barcode.polygon], np.int32)
                #modificar arreglo pts
                pts = pts.reshape((-1, 1, 2))
                
                #crear cuadro de color segun estado
                cv2.polylines(img,     #imagen
                               [pts],  #coordenadas
                                True,  #poligono cerrado
                                color, #color de cuadro
                                5)     #espesor de cuadro
                
                #formar/crear segundo cuadro para mostrar texto
                pts2 = barcode.rect
                #colocar texto en el cuadro
                cv2.putText(img,                        #imagen
                            myoutput,                   #texto
                            (pts2[0],pts2[1]),          #coordenadas
                            cv2.FONT_HERSHEY_SIMPLEX,   #tipo de letra
                            0.9,                        #tamano de letra
                            color,                      #color letra
                            3)                          #espesor letra
            #mostrar imagen 
            cv2.imshow('Result', img)
            #esperar 1ms para terminar camara
            cv2.waitKey(1)
        self.closeWin(cv2)
        db1.close()
        
    def closeWin(self, cv):
        cv.destroyAllWindows()
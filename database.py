import pymysql

class DataBase():
    
    mat = []
    
    def __init__(self):
        self.connection  = pymysql.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'root007',
            db = 'biblioteca'
            )
        
        self.cursor = self.connection.cursor()
        print('conexion [ok]')
        
        
    def select(self, id, sintax):
        #sint = "SELECT nombre FROM gur WHERE curp = '{0}'"
        
        sql = sintax.format(id)
        
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            #print("nombre: {0}".format(user[0]))
            self.mat += {user[0]}   #nombre
            self.mat += {user[1]}   #apP
            self.mat += {user[2]}   #apM
            self.mat += {user[3]}   #edad
            
            self.mat += {user[4]}   #localidad
            self.mat += {user[5]}   #curp
            #self.mat += {user[6]}   #direccion
            self.mat += {user[6]}   #telefono
            #self.mat += {user[8]}   #mail
            #self.mat += {user[9]}   #tipo
            #self.mat += {user[10]}  #pass
            #self.mat += {user[11]}  #pass
            
        except Exception as e:
            print('ha ocurrido un error en consulta a base de datos [select]')
            #raise
    def selectONE(self, id, sintax):
        #sint = "SELECT nombre FROM gur WHERE curp = '{0}'"
        valor = ''
        sql = sintax.format(id)
        
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            
            valor = user[0]
            
        except Exception as e:
            print('ha ocurrido un error en consulta a base de datos [select]')
            #raise
        return valor
    def select_all(self):
        sql = 'SELECT id, nombre FROM table1'
        
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                print('id: {0}, nombre: {1}\n'.format(user[0], user[1]))
        except Exception as e:
            raise
        
    def update(self, id, nombre):
        sql = "UPDATE table1 SET nombre = '{0}' WHERE id = {1}".format(nombre, id)
        
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    def inssert(self, mat):
        sql = "INSERT INTO gur VALUES ('{0}', '{1}','{2}',{3},'{4}','{5}','{6}',{7},'{8}','{9}','{10}','{11}')".format(
            mat[0],mat[1],mat[2],mat[3],mat[4],mat[5],mat[6],mat[7],mat[8],mat[9],mat[10],mat[11])
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
    def close(self):
        print('conexion [close]')
        self.connection.close()
    
#db = DataBase()
#db.select('AAPC000607HQRBCRA5')
#db.select_all()
#db.update(2, 'chencho')
#mat = ['1', '2', '3', 4, '5', '6', '7', 8, '9','10','11','12']
#db.inssert(mat)

#db.close()
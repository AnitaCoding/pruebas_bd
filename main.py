import sqlite3
'''
conexion = sqlite3.connect('inicio_bd.db') #conectar a la bd

#para poder modificar datos obtenidos
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()#Creamos cursor, es un objeto para ejecutar las sentencias de la bd

respuesta = cursor.execute('SELECT * FROM persona;') #ejecutar la sentencia sql
#print('respuesta simple ', respuesta.fetchall())

resultado = [dict(fila) for fila in respuesta.fetchall()] #Esto pinta el resultado como lista de diccionarios
print('resultado bonito ', resultado)
'''
def format(respuesta):
    result = []

    for fila in respuesta.fetchall():
        result.append(dict(fila))

    print(result)

class Conexion:
    def __init__(self, query_sql, param = []):
        self.con = sqlite3.connect('inicio_bd.db')
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.res = self.cur.execute(query_sql, param)

conexion_select = Conexion('SELECT * FROM persona;')
respuesta = conexion_select.res
format(respuesta)
conexion_select.con.close()

conexion_select_by = Conexion('SELECT * FROM persona WHERE id= 1')
respuesta2 = conexion_select_by.res
format(respuesta2)
conexion_select_by.con.close()

conexion_insert = Conexion('INSERT INTO persona(name, lastname, dni, email) VALUES (?,?,?,?);', ['Fernando', 'Guerrero', '54321789M', 'elfer@gmail.com'])
respuesta3 = conexion_insert.res
conexion_insert.con.commit()#para confirmar guardado
conexion_insert.con.close()
from sqlite3 import *
def crearConexion():
    conn = connect('./base_datos/tecnologico.db')
    con.commit() #confirmamos la conexion
    conn.close() #cerramos la conexion

def crearTablaAlumno(nombre, edad):
    conn = connect('./base_datos/tecnologico.db')
    cursor = conn.cursor()
    sentencia = f"INSERT INTO Alumnos(nombre, edad) VALUES(?,?)"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
def insertTablaAlumno(lista):
    conn = connect('./base_datos/tecnologico.db')
    cursor = conn.cursor()
    sentencia = f"INSERT INTO Alumnos(nombre, edad) VALUES(?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()

if __name__=='__main__': #se inicializa solo
    #crear conexion
    listaAlumno = [
        ('edwin',20),
        ('yerald',3)
    ]
    # crearTablaAlumno('jory', 20)
    # crearTablaAlumno('chinin', 20)
    # crearTablaCurso()
    insertTablaAlumno(listaAlumno)
#hacer borrar y actualizar
import sqlite3 
minConexion = sqlite3.connect("primeraBase")

miCursos=minConexion.cursor()

#miCursos.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursos.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")
minConexion.commit()

minConexion.close()

import sqlite3 
minConexion = sqlite3.connect("primeraBase")

miCursos=minConexion.cursor()

#miCursos.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursos.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")

#variosproductos=[
#    ("camiseta",10,"deportes"),
#    ("jarrón",90,"ceramica"),
#    ("camión",10,"jugueteria")
#]

#miCursos.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosproductos)

miCursos.execute("SELECT * FROM PRODUCTOS")

variosproductos2=miCursos.fetchall()

#print(variosproductos2)

for productos in variosproductos2:
    print(productos[1])

minConexion.commit()

minConexion.close()

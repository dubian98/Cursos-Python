import sqlite3
miConexion=sqlite3.connect("gestionProductos2")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[
    ("Pelota",20,"Jugueteria"),
    ("Pantalón",15,"Confección"),
    ("Destornillador",25,"Ferreteria"),
    ("Destornilladores",15,"Ferreteria"),
    ("Jarron",45,"Cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

miConexion.commit()

miConexion.close()


#--------------segunda parte solo read----------

import sqlite3
miConexion=sqlite3.connect("gestionProductos2")

miCursor=miConexion.cursor()


miCursor.execute("SELECT * FROM PRODUCTOS WHERE ID=1")
#miCursor.execute("UPDATE PRODUCTOS  SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota' ")
#miCursor.execute("DELETE FROM PRODUCTOS  WHERE ID=4 ")


productos=miCursor.fetchall()
print(productos)

miConexion.commit()

miConexion.close()
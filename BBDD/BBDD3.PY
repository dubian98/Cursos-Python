import sqlite3
miConexion=sqlite3.connect("gestionProductos")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[
    ("Pelota",20,"Jugueteria"),
    ("Pantalón",15,"Confección"),
    ("Destornillador",25,"Ferreteria"),
    ("Jarron",45,"Cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

miConexion.commit()

miConexion.close()
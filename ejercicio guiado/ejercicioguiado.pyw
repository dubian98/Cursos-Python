from tkinter import *
from tkinter import messagebox
import sqlite3 
conexion=sqlite3.connect("ejercicio_guiado")
micursor=conexion.cursor()
raiz = Tk()
raiz.title("Formulario")


#-------------crear al base de datos------------
def generar():
    try:
        conexion=sqlite3.connect("ejercicio_guiado")
        micursor=conexion.cursor()    
        micursor.execute('''
            CREATE TABLE USUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            CONTRASEÑA VARCHAR(50),
            APELLIDO VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(50))
        ''')
        conexion.commit()
        conexion.close()
    except sqlite3.OperationalError:
        messagebox.showinfo("la base de datos ya existe")
#-----------limpiar pantalla--------
def limpiar():
    x1.set("")
    x2.set("")
    x3.set("")
    x4.set("")
    x5.set("")
    x6.set("")
#----------cerrar documento---------------
def info_salir():
    
    valor = messagebox.askokcancel("salir","¿Deseas salir de la aplicacion?")
    if valor == True:
        raiz.destroy()
#------------Agregar datos ------------

def insertar(num,con,ape,dire,com):
    conexion=sqlite3.connect("ejercicio_guiado")
    micursor=conexion.cursor()
    print(num,con,ape,dire,com)
    lista=[(num,con,ape,dire,com)]
    print(lista)
    micursor.executemany("INSERT INTO USUARIOS VALUES(NULL,?,?,?,?,?)",lista)
    conexion.commit()
    conexion.close()

#----------Leer datos------------
def leer(num1):
    conexion=sqlite3.connect("ejercicio_guiado")
    micursor=conexion.cursor()    
    
    micursor.execute("SELECT * FROM USUARIOS WHERE ID= (?)")

    usuario=micursor.fetchall()
    print(usuario)

    conexion.commit()
    conexion.close()

#---------------actualizar valores-----------
def actualizar(num1):
    conexion=sqlite3.connect("ejercicio_guiado")
    micursor=conexion.cursor()    
    micursor.execute("UPDATE * FROM USUARIOS  WHERE ID=num1 ")
#miCursor.execute("DELETE FROM PRODUCTOS  WHERE ID=4 ")

    conexion.commit()
    conexion.close()

#-----------------Borrar valores
def borrar(num1):
    conexion=sqlite3.connect("ejercicio_guiado")
    micursor=conexion.cursor()    
    miCursor.execute("DELETE * FROM USUARIOS WHERE ID=num1 ")

    usuario=micursor.fetchall()
    print(usuario)

    conexion.commit()
    conexion.close()

#-----------creación de la raiz
barra_menu=Menu(raiz)


raiz.config(menu=barra_menu,width=400,height=400)
#--------------menu----------------
BBDD_menu=Menu(barra_menu,tearoff=0)
BBDD_menu.add_command(label="Crear BBDD",command=lambda:generar())
BBDD_menu.add_command(label="Salir",command=lambda:info_salir())
BORRAR_menu=Menu(barra_menu,tearoff=0)
BORRAR_menu.add_command(label="Borrar",command=lambda:limpiar())
CRUD_menu=Menu(barra_menu,tearoff=0)
CRUD_menu.add_command(label="crear",command=lambda:insertar(x1.get(),x2.get(),x3.get(),x4.get(),x5.get()))
CRUD_menu.add_command(label="Leer",command=lambda:leer(x6.get()))
CRUD_menu.add_command(label="Actualizar",command=lambda:actualizar(x6.get()))
CRUD_menu.add_command(label="Borrar",command=lambda:borrar(x6.get()))
AYUDA_menu=Menu(barra_menu,tearoff=0)
AYUDA_menu.add_command(label="Acerca de")
AYUDA_menu.add_command(label="Licencia")

#-----------asignacion de funsiones a menu----------

barra_menu.add_cascade(label="BBDD",menu=BBDD_menu)
barra_menu.add_cascade(label="BORRAR",menu=BORRAR_menu)
barra_menu.add_cascade(label="CRUD",menu=CRUD_menu)
barra_menu.add_cascade(label="AYUDA",menu=AYUDA_menu)
#---------------cuadros de dialogo----------
usuario=Label(raiz,text="Usuario")
usuario.grid(row=0,column=0,columnspan=2)
contraseña=Label(raiz,text="Contraseña")
contraseña.grid(row=1,column=0,padx=10,pady=10,columnspan=2)
apellido=Label(raiz,text="Apellido")
apellido.grid(row=2,column=0,padx=10,pady=10,columnspan=2)
direccion=Label(raiz,text="Dirección")
direccion.grid(row=3,column=0,padx=10,pady=10,columnspan=2)
comentarios=Label(raiz,text="Comentarios")
comentarios.grid(row=4,column=0,padx=10,pady=10,columnspan=2)
ID_=Label(raiz,text="ID")
ID_.grid(row=5,column=0,columnspan=2)
#---------cuadros de texto---------
x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
x6=StringVar()


nombretexto=Entry(raiz,textvariable=x1)
nombretexto.grid(row=0,column=3,padx=10,pady=10,columnspan=2)
contraseñatexto=Entry(raiz,textvariable=x2)
contraseñatexto.grid(row=1,column=3,padx=10,pady=10,columnspan=2)
apellidotexto=Entry(raiz,textvariable=x3)
apellidotexto.grid(row=2,column=3,padx=10,pady=10,columnspan=2)
direcciontexto=Entry(raiz,textvariable=x4)
direcciontexto.grid(row=3,column=3,padx=10,pady=10,columnspan=2)
comentariostexto=Entry(raiz,textvariable=x5)
comentariostexto.grid(row=4,column=3,padx=10,pady=10,columnspan=2)
idtexto=Entry(raiz,textvariable=x6)
idtexto.grid(row=5,column=3,padx=10,pady=10,columnspan=2)


#-----------botones-----------
create=Button(raiz,text="Create",command=lambda:insertar(x1.get(),x2.get(),x3.get(),x4.get(),x5.get()))
create.grid(row=6,column=0,padx=10,pady=10)
read=Button(raiz,text="Read",command=lambda:leer(x6.get()))
read.grid(row=6,column=1,padx=10,pady=10)
update=Button(raiz,text="Upade",command=lambda:actualizar(x6.get()))
update.grid(row=6,column=3,padx=10,pady=10)
delete=Button(raiz,text="Delete",command=lambda:borrar(x6.get()))
delete.grid(row=6,column=4,padx=10,pady=10)
conexion.close()

raiz.mainloop()


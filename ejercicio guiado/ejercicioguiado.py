from tkinter import *
raiz = Tk()
raiz.title("Formulario")
#raiz.geometry("250x350")

barra_menu=Menu(raiz)
#-----------creación de la raiz

raiz.config(menu=barra_menu,width=400,height=400)
#--------------menu----------------
BBDD_menu=Menu(barra_menu,tearoff=0)
BBDD_menu.add_command(label="Crear BBDD")
BBDD_menu.add_command(label="Salir")
BORRAR_menu=Menu(barra_menu,tearoff=0)
BORRAR_menu.add_command(label="Borrar")
CRUD_menu=Menu(barra_menu,tearoff=0)
CRUD_menu.add_command(label="crear")
CRUD_menu.add_command(label="Leer")
CRUD_menu.add_command(label="Actualizar")
CRUD_menu.add_command(label="borrar")
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

#---------cuadros de texto---------
nombretexto=Entry(raiz)
nombretexto.grid(row=0,column=3,padx=10,pady=10,columnspan=2)
contraseñatexto=Entry(raiz)
contraseñatexto.grid(row=1,column=3,padx=10,pady=10,columnspan=2)
apellidotexto=Entry(raiz)
apellidotexto.grid(row=2,column=3,padx=10,pady=10,columnspan=2)
direcciontexto=Entry(raiz)
direcciontexto.grid(row=3,column=3,padx=10,pady=10,columnspan=2)
comentariostexto=Entry(raiz)
comentariostexto.grid(row=4,column=3,padx=10,pady=10,columnspan=2)

#-----------botones-----------
create=Button(raiz,text="Create")
create.grid(row=5,column=0,padx=10,pady=10)
read=Button(raiz,text="Read")
read.grid(row=5,column=1,padx=10,pady=10)
update=Button(raiz,text="Upade")
update.grid(row=5,column=3,padx=10,pady=10)
delete=Button(raiz,text="Delete")
delete.grid(row=5,column=4,padx=10,pady=10)

raiz.mainloop()


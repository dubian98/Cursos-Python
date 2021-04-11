from tkinter import *
from tkinter import messagebox
root=Tk()

def info_adicional():
    messagebox.showinfo("procesadorde dubian","procesador de texto 2021")

def info_licencia():
    messagebox.showwarning("licencia","producto bajo licencia generica")

def info_salir():
    #valor = messagebox.askquestion("salir","¿Deseas salir de la aplicacion?")
    valor = messagebox.askokcancel("salir","¿Deseas salir de la aplicacion?")
    if valor == True:
        root.destroy()

def cerrar_documento():
    valor = messagebox.askretrycancel("reintentar","no es posible cerrar")
    if valor == False:
        root.destroy()

barramenu=Menu(root)
root.config(menu=barramenu,width=300,height=300)

archivo_menu=Menu(barramenu,tearoff=0)
archivo_menu.add_command(label="nuevo")
archivo_menu.add_command(label="guardar")
archivo_menu.add_command(label="cerrar", command=lambda:cerrar_documento())
archivo_menu.add_separator()
archivo_menu.add_command(label="salir", command=lambda:info_salir())

edicion_menu=Menu(barramenu,tearoff=0)
edicion_menu.add_command(label="copiar")
edicion_menu.add_command(label="cortar")
edicion_menu.add_command(label="pegar")


herramientas_menu=Menu(barramenu,tearoff=0)


ayuda_menu=Menu(barramenu,tearoff=0)
ayuda_menu.add_command(label="licencia",command=lambda:info_licencia())
ayuda_menu.add_command(label="acercar de",command=lambda:info_adicional())

barramenu.add_cascade(label="archivo",menu=archivo_menu)
barramenu.add_cascade(label="edición",menu=edicion_menu)
barramenu.add_cascade(label="Herramientas",menu=herramientas_menu)
barramenu.add_cascade(label="Ayuda",menu=ayuda_menu)

root.mainloop()
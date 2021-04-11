from tkinter import *
root=Tk()

barramenu=Menu(root)
root.config(menu=barramenu,width=300,height=300)

archivo_menu=Menu(barramenu,tearoff=0)
archivo_menu.add_command(label="nuevo")
archivo_menu.add_command(label="guardar")
archivo_menu.add_command(label="cerrar")
archivo_menu.add_separator()
archivo_menu.add_command(label="salir")

edicion_menu=Menu(barramenu,tearoff=0)
edicion_menu.add_command(label="copiar")
edicion_menu.add_command(label="cortar")
edicion_menu.add_command(label="pegar")


herramientas_menu=Menu(barramenu,tearoff=0)


ayuda_menu=Menu(barramenu,tearoff=0)
ayuda_menu.add_command(label="licencia")
ayuda_menu.add_command(label="acercar de")

barramenu.add_cascade(label="archivo",menu=archivo_menu)
barramenu.add_cascade(label="edición",menu=edicion_menu)
barramenu.add_cascade(label="Herramientas",menu=herramientas_menu)
barramenu.add_cascade(label="Ayuda",menu=ayuda_menu)

root.mainloop()
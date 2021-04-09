from tkinter import *

raiz = Tk()

miframe = Frame(raiz, width =1200 , height=600)
miframe.pack()


cuadroNombre =Entry(miframe)
cuadroNombre.config(bg="blue")
cuadroNombre.grid(row=0,column=1,padx=10, pady=10)

nombrelabel = Label(miframe, text="Nombre: ")
nombrelabel.grid(row=0,column=0,sticky="w",padx=10, pady=10)

cuadroPass =Entry(miframe)
cuadroPass.grid(row=4,column=1,padx=10, pady=10)
cuadroPass.config(show="?")

Passlabel = Label(miframe, text="contraseña: ")
Passlabel.grid(row=4,column=0,sticky="w",padx=10, pady=10)


cuadroApellido =Entry(miframe)
cuadroApellido.grid(row=1,column=1,padx=10, pady=10)

Apellidolabel = Label(miframe, text="Apellido: ")
Apellidolabel.grid(row=1,column=0,sticky="w",padx=10, pady=10)

cuadroDireccion =Entry(miframe)
cuadroDireccion.grid(row=2,column=1,padx=10, pady=10)

Direccionlabel = Label(miframe, text="Dirección de casa: ")
Direccionlabel.grid(row=2,column=0,sticky="w",padx=10, pady=10)

raiz.mainloop()
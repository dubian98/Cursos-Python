from tkinter import *

raiz = Tk()

miframe = Frame(raiz, width =1200 , height=600)
miframe.pack()

minombre=StringVar()

cuadroNombre =Entry(miframe, textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=10, pady=10)

cuadroPass =Entry(miframe)
cuadroPass.grid(row=3,column=1,padx=10, pady=10)
cuadroPass.config(show="?")

cuadroApellido =Entry(miframe)
cuadroApellido.grid(row=1,column=1,padx=10, pady=10)

cuadroDireccion =Entry(miframe)
cuadroDireccion.grid(row=2,column=1,padx=10, pady=10)

textoComentario =Text(miframe, width=16, height =16)
textoComentario.grid(row=4,column=1)

scrollvert=Scrollbar(miframe,command=textoComentario.yview)
scrollvert.grid(row=4,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollvert.set)

nombrelabel = Label(miframe, text="Nombre: ")
nombrelabel.grid(row=0,column=0,sticky="w",padx=10, pady=10)

Apellidolabel = Label(miframe, text="Apellido: ")
Apellidolabel.grid(row=1,column=0,sticky="w",padx=10, pady=10)

Passlabel = Label(miframe, text="contraseña: ")
Passlabel.grid(row=3,column=0,sticky="w",padx=10, pady=10)

Direccionlabel = Label(miframe, text="Dirección: ")
Direccionlabel.grid(row=2,column=0,sticky="w",padx=10, pady=10)

comentarioslabel = Label(miframe, text="Comentarios: ")
comentarioslabel.grid(row=4,column=0,sticky="w",padx=10, pady=10)

def codigoBoton():

    minombre.set("dubian")

butonEnvio =Button(miframe, text="enviar",command=codigoBoton)
butonEnvio.grid(row=5,column=3)


raiz.mainloop()
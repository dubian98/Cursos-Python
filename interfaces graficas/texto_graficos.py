from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.iconbitmap("icono.ico")

raiz.config(bg="gray")

miframe = Frame(raiz, width=500, height=400)

miframe.pack()

miframe.config(bg="red")

#milabel = Label(miframe, text="hola mundo nuevo")
#milabel.place(x=100,y=200)
miimagen=PhotoImage(file="descarga.png")
Label(miframe, image= miimagen).place(x=100,y=200)

miframe.config(cursor="pirate")

raiz.mainloop()

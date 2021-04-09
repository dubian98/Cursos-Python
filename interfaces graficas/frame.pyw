from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(1,0)

raiz.iconbitmap("icono.ico")

#raiz.geometry("650x350")

raiz.config(bg="yellow")

raiz.config(bd=40)

raiz.config(relief="sunken")
raiz.config(cursor="hand2")

miframe = Frame()

#miframe.pack(side="left", anchor="n")

miframe.pack()

miframe.config(bg="red")


miframe.config(width="650",height="350")

miframe.config(bd=30)

miframe.config(relief="groove")
miframe.config(cursor="pirate")

raiz.mainloop()

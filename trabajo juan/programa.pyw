from tkinter import *

raiz = Tk()
raiz.title("Registro área de montaje")
Frame1 = Frame(raiz)
Frame1.pack()
titulo=Label(Frame1,text="Sistema de registro de actividades en el área de pegado",padx=10,pady=10)
titulo.config(background="black",fg="white")
titulo.pack()
Frame2 = Frame(raiz)
Frame2.pack()
#-------------Etiquetas-----------------------
cuadro1=Label(Frame2,text="Activida")
cuadro1.grid(row=0,column=0)
cuadro1.config(background="red",fg="white")

cuadro2=Label(Frame2,text="Nombre Operario")
cuadro2.grid(row=1,column=0)
cuadro2.config(background="red",fg="white")

cuadro3=Label(Frame2,text="Turno")
cuadro3.grid(row=2,column=0)
cuadro3.config(background="red",fg="white")

cuadro4=Label(Frame2,text="Montadora")
cuadro4.grid(row=3,column=0)
cuadro4.config(background="red",fg="white")

cuadro5=Label(Frame2,text="Parte")
cuadro5.grid(row=4,column=0)
cuadro5.config(background="red",fg="white")

cuadro6=Label(Frame2,text="Maquina")
cuadro6.grid(row=5,column=0)
cuadro6.config(background="red",fg="white")

cuadro7=Label(Frame2,text="Desarrollo (mm)")
cuadro7.grid(row=6,column=0)
cuadro7.config(background="red",fg="white")

cuadro8=Label(Frame2,text="No. Clises por manga")
cuadro8.grid(row=7,column=0)
cuadro8.config(background="red",fg="white")

cuadro9=Label(Frame2,text="No. De mangas a utilizar (Incluye fondeadora)")
cuadro9.grid(row=8,column=0)
cuadro9.config(background="red",fg="white")

cuadro10=Label(Frame2,text="¿Lleva manga fondeadora?")
cuadro10.grid(row=9,column=0)
cuadro10.config(background="red",fg="white")

cuadro11=Label(Frame2,text="No. De mangas con cinta reutilizada")
cuadro11.grid(row=10,column=0)
cuadro11.config(background="red",fg="white")

cuadro12=Label(Frame2,text="Ancho de cinta (mm)")
cuadro12.grid(row=11,column=0)
cuadro12.config(background="red",fg="white")

cuadro13=Label(Frame2,text="Marca cinta (3M, Tesa o Mix)")
cuadro13.grid(row=12,column=0)
cuadro13.config(background="red",fg="white")

cuadro14=Label(Frame2,text="Cambio (Observaciones)")
cuadro14.grid(row=13,column=0)
cuadro14.config(background="red",fg="white")

cuadro15=Label(Frame2,text="Motivo de cambio")
cuadro15.grid(row=14,column=0)
cuadro15.config(background="red")

# -----------------Cuadros de texto--------------------------
Texto1=Entry(Frame2)
Texto1.grid(row=0,column=1)

Texto2=Entry(Frame2)
Texto2.grid(row=1,column=1)

Texto3=Entry(Frame2)
Texto3.grid(row=2,column=1)

Texto4=Entry(Frame2)
Texto4.grid(row=3,column=1)

Texto5=Entry(Frame2)
Texto5.grid(row=4,column=1)

Texto6=Entry(Frame2)
Texto6.grid(row=5,column=1)

Texto7=Entry(Frame2)
Texto7.grid(row=6,column=1)

Texto8=Entry(Frame2)
Texto8.grid(row=7,column=1)

Texto9=Entry(Frame2)
Texto9.grid(row=8,column=1)

Texto10=Entry(Frame2)
Texto10.grid(row=9,column=1)

Texto11=Entry(Frame2)
Texto11.grid(row=10,column=1)

Texto12=Entry(Frame2)
Texto12.grid(row=11,column=1)

Texto13=Entry(Frame2)
Texto13.grid(row=12,column=1)

Texto14=Entry(Frame2)
Texto14.grid(row=13,column=1)

Texto15=Entry(Frame2)
Texto15.grid(row=14,column=1)



raiz.mainloop()
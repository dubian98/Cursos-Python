from tkinter import *

fondo=Tk()
texto=""

def revisar(num):
    print("esta funcionando")
    global texto
    if 1>num>20:
        texto="el numero debe ser entre 1 y 20"
        print("el numero debe ser entre 1 y 20")
    elif num<12:
        texto="el numero secreto es mayor"
        print("el numero secreto es mayor")
    elif num>12:
        texto="el numero secreto es menor"
        print("el numero secreto es menor")
    else:
        texto="felicitaciones adivinaste, el numero era 12"
        print("felicitaciones adivinaste, el numero era 12")
    cuadro4.config(text=texto,bg="yellow",fg="black")

pantalla=StringVar()
cuadro1=Label(fondo,text="Adivina el numero [1-20]: " ,width=20)
cuadro1.grid(row=0,column=1, padx=10, pady=10, columnspan=2)
cuadro1.config(bg="gray",fg="yellow")

cuadro2=Label(fondo,text="Escribe el numero: " ,width=20)
cuadro2.grid(row=1,column=1, padx=10, pady=10)
cuadro2.config(bg="black",fg="green")

cuadro3=Entry(fondo ,textvariable=pantalla,width=20)
cuadro3.grid(row=1,column=2, padx=10, pady=10)
cuadro3.config(bg="pink",fg="green")

cuadro4=Label(fondo)
cuadro4.grid(row=3,column=0, padx=10, pady=10,columnspan=2)


boton1=Button(fondo,text="Comprobar",command=lambda:revisar(int(pantalla.get())))
boton1.grid(row=2,column=2)

fondo.mainloop()
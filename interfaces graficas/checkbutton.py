from tkinter import *

root = Tk()
root.title("ejemplo")

playa=IntVar()
montana=IntVar()
rural=IntVar()

def opcionesvije():
    opcionesEscojidas=""

    if(playa.get()==1):
        opcionesEscojidas+=" playa"

    if(montana.get()==1):
        opcionesEscojidas+=" montaña"
    if(rural.get()==1):
        opcionesEscojidas+=" Turismo rural"
    TExtofinal.config(text=opcionesEscojidas)
foto=PhotoImage(file="avion1.png")
Label(root, image=foto).pack()


frame=Frame(root)
frame.pack()

Label(frame, text="elige destinos", width=50 ).pack()

Checkbutton(root,text="playa",variable=playa,onvalue=1,offvalue=0,command=opcionesvije).pack()
Checkbutton(root,text="montaña",variable=montana,onvalue=1,offvalue=0,command=opcionesvije).pack()
Checkbutton(root,text="rural",variable=rural,onvalue=1,offvalue=0,command=opcionesvije).pack()

TExtofinal=Label(frame)
TExtofinal.pack()

root.mainloop()
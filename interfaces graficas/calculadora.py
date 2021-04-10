from tkinter import *

fondo = Tk()

Frame1 = Frame(fondo, width =200 , height=300)
Frame1.pack()

operacion=""
resultados=0
#----------------------pantalla---------------------------

numeropantalla=StringVar()

respuesta =Entry(Frame1,textvariable=numeropantalla)
respuesta.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
respuesta.config(background="black", fg="#03f943", justify="right")

#----------------------pulsaciones teclado-------------

def numeropulsado(num):
    global operacion
    if operacion !="":
        numeropantalla.set(num)
        operacion=""
    else:
        numeropantalla.set(numeropantalla.get()+num)

#-----------------------funcion suma-------------
def sumar(num):
    global operacion 
    global resultados
    resultados+=float(num)
    operacion="suma"
    numeropantalla.set(resultados)

#-------------------funcion elresultado-------------
def elresultado():
    global resultados
    numeropantalla.set(resultados+float(numeropantalla.get()))
    resultados=0
#----------------------fila 1-------------------------

b1=Button(Frame1, text="1" , width=3,command=lambda:numeropulsado("1"))
b1.grid(row=1, column=0,padx=2, pady=2)

b2=Button(Frame1, text="2" , width=3,command=lambda:numeropulsado("2"))
b2.grid(row=1, column=1,padx=2, pady=2)

b3=Button(Frame1, text="3", width=3,command=lambda:numeropulsado("3") )
b3.grid(row=1, column=2,padx=2, pady=2)

dividir=Button(Frame1, text="/", width=3 )
dividir.grid(row=1, column=3,padx=2, pady=2)


#---------------fila 2-----------------------

b4=Button(Frame1, text="4" , width=3,command=lambda:numeropulsado("4"))
b4.grid(row=2, column=0,padx=2, pady=2)

b5=Button(Frame1, text="5", width=3,command=lambda:numeropulsado("5") )
b5.grid(row=2, column=1,padx=2, pady=2)

b6=Button(Frame1, text="6" , width=3,command=lambda:numeropulsado("6"))
b6.grid(row=2, column=2,padx=2, pady=2)

multiplicar=Button(Frame1, text="*", width=3 ,command=lambda:numeropulsado("6"))
multiplicar.grid(row=2, column=3,padx=2, pady=2)

#---------------fila 3-----------------------

b7=Button(Frame1, text="7" , width=3,command=lambda:numeropulsado("7"))
b7.grid(row=3, column=0,padx=2, pady=2)

b8=Button(Frame1, text="8" , width=3,command=lambda:numeropulsado("8"))
b8.grid(row=3, column=1,padx=2, pady=2)

b9=Button(Frame1, text="9", width=3,command=lambda:numeropulsado("9") )
b9.grid(row=3, column=2,padx=2, pady=2)

restar=Button(Frame1, text="-", width=3 )
restar.grid(row=3, column=3,padx=2, pady=2)

#---------------fila 4-----------------------

b0=Button(Frame1, text="0" , width=3,command=lambda:numeropulsado("0"))
b0.grid(row=4, column=0,padx=2, pady=2)
coma=Button(Frame1, text="," , width=3)
coma.grid(row=4, column=1,padx=2, pady=2)
suma=Button(Frame1, text="+" , width=3,command=lambda:sumar(numeropantalla.get()))
suma.grid(row=4, column=2,padx=2, pady=2)
igual=Button(Frame1, text="=" , width=3, command=lambda:elresultado())
igual.grid(row=4, column=3,padx=2, pady=2)

borrar=Button(Frame1, text="borrar" )
borrar.grid(row=5, column=3,padx=2, pady=2)

fondo.mainloop()
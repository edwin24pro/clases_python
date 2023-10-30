from tkinter import *
ventana = Tk()
ventana.geometry('250x170')
ventana.config(bg='pink')
operacion = IntVar()
def mostrar():
    opcion=operacion.get()
    if opcion == 1:
        resultadosuma = int(cuadronum1.get()) + int(cuadronum2.get())
        cuadrototal.config(fg='white')
        cuadrototal.delete(0, END)
        cuadrototal.insert(0,resultadosuma)
    elif opcion==2:
        resultadoresta = int(cuadronum1.get()) - int(cuadronum2.get())
        cuadrototal.config(fg='white')
        cuadrototal.delete(0, END)
        cuadrototal.insert(0,resultadoresta)
    elif opcion==3:
        resultadomultipli = int(cuadronum1.get()) * int(cuadronum2.get())
        cuadrototal.config(fg='white')
        cuadrototal.delete(0, END)
        cuadrototal.insert(0,resultadomultipli)
    elif opcion==4:
        resultadodivi = int(cuadronum1.get()) / int(cuadronum2.get())
        cuadrototal.config(fg='white')
        cuadrototal.delete(0, END)
        cuadrototal.insert(0,resultadodivi)
    else:
        cuadrototal.config(fg='red')
        cuadrototal.insert(0,'error!')

def eliminar():
    cuadronum1.delete(0, END)
    cuadronum2.delete(0, END)
    cuadrototal.delete(0, END)
    cuadrototal.config(fg='yellow')
    cuadrototal.insert(0, 'eliminado!')


etiquetannum1 = Label(ventana, text='ingrese un numero')
cuadronum1 = Entry(ventana, bg='#fff999', width='5')
cuadronum1.focus()
etiquetannum2 = Label(ventana, text= 'ingrese otro numero')
cuadronum2 = Entry(ventana, bg='#fff999', width='5')
etiquetatotal = Label(ventana, text='Total', font='Impact')
cuadrototal= Entry(ventana, bg='purple', fg='white')

etiquetannum1.grid(row=0, column= 0)
cuadronum1.grid(row=1, column=0)
etiquetannum2.grid(row=2, column=0)
cuadronum2.grid(row=3, column=0, padx='20')
etiquetatotal.grid(row=4, column=0)
cuadrototal.grid(row=5, column=0)

frame_particion = Frame(ventana, bg='pink', height=170)
frame_particion.grid(row=0, column=1, ipadx=10, rowspan=7)

buttonsuma = Radiobutton(ventana, text='suma', value=1, variable=operacion)
buttonrestar = Radiobutton(ventana, text='restar', value=2, variable=operacion)
buttonmulti = Radiobutton(ventana, text='Multiplicar', value=3, variable=operacion)
buttondivision = Radiobutton(ventana, text='Dividir', value=4, variable=operacion)

buttonsuma.grid(row=1, column=3)
buttonrestar.grid(row=2, column=3)
buttonmulti.grid(row=3, column=3)
buttondivision.grid(row=4, column=3)

botoncalcular = Button(ventana, text='calcular', command=mostrar, fg='green')
boton_eliminar = Button(ventana, text='eliminar', command = eliminar, fg='red')

botoncalcular.grid(row=6, column=0)
boton_eliminar.grid(row=6, column=3)

ventana.mainloop()
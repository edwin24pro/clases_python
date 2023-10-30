##Radiobutons
from tkinter import *
ventana = Tk()
ventana.title('clase radio button')
ventana.geometry('600x400')
#Instancias la clase radiobuton
frame_genero = Frame(ventana, bg='yellow', width='150', height='100')
frame_genero.pack(side=LEFT)

frame_pais = Frame(ventana, bg='orange', width='150', height='100')
frame_pais.pack(side=RIGHT)

info = IntVar()
def mostrar_radio():
    valor = info.get()
    etiqueta2.config(text=f'eres {valor} ')


radioMasculino = Radiobutton(frame_genero,text='Masculino', value=1, variable=info)
radioMasculino.pack(side=LEFT)
radioFemenino = Radiobutton(frame_genero,text='Femenino', value=2, variable=info)
radioFemenino.pack()

#radiioButton paises
radioPeru = Radiobutton(frame_pais, text='Perú', value=1, variable=info)
radioPeru.pack(side=LEFT)
radioargentina = Radiobutton(frame_pais, text='Argentina', value=2, variable=info)
radioPeru.pack(side=LEFT)

boton_mostrar = Button(ventana, text='mostrar', command=mostrar_radio)
boton_mostrar.pack(side=BOTTOM)

etiqueta2 = Label(ventana)
etiqueta2.pack()


ventana.mainloop()
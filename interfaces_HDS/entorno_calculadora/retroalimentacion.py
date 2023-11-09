'''from tkinter import *


def enter():
    if cuadro.get() == '1':
        cuadro.delete(0, END)
        cuadro.insert(0,'Bien')
ventana = Tk()
ventana.resizable(0,0) #bloquea la ventana
ventana.config(cursor='pirate')
cuadro = Entry(ventana, font=('arial',16,'bold'))#font te permite cambiar el tipo, tamaño, estilo de letra
boton_enter = Button(ventana, text='<---', command=enter)

cuadro.pack()
boton_enter.pack()
ventana.mainloop()'''
from tkinter import *
ws=Tk()
def nueva_ventana():
    ventana = Tk()
    saludo = Label(text='bienvenido a la nueva ventana').pack()
    ventana.mainloop()

def task():
    ws.destroy()
    nueva_ventana()
    
ws.geometry("200x200")

button=Button(ws,text="On Clicking Quit",command= task)

button.focus()
button.pack(expand=True)


ws.mainloop()

    
variable()
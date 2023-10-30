##crear dos etiqueta
from tkinter import*

##Funciones
def eliminar():
    cuadro_ingresar_num.delete(0,END)
    cuadro_ingresar_num_2.delete(0,END)
    cuadro_resultado.delete(0,END)
    cuadro_promedio.delete(0, END)
    cuadro_ingresar_num.focus()

def suma():
    signo = ''
    num1 = int(cuadro_ingresar_num.get())
    num2 = int(cuadro_ingresar_num_2.get())
    resul = num1 + num2
    cuadro_resultado.delete(0,END)
    cuadro_resultado.insert(0, resul)

def promedio():
    datos = cuadro_promedio.get()
    cont = 0
    for i in datos:
        if i == '+':
            cont += 1

    resul = int(len(datos)) - cont
    promedio = eval(datos) / resul
    cuadro_promedio.delete(0, END)
    cuadro_promedio.insert(0, promedio)

def insert_signo(signo):
    casa = cuadro_promedio.get()
    longitud = len(casa) +1
    cuadro_promedio.insert(longitud, signo)

ventana = Tk('300x300')
##etiquetas
etiqueta_ingresar_num = Label(ventana, text='Ingrese un número: ').grid(row='0', column='0')
etiqueta_ingresar_num_dos = Label(ventana, text='Ingrese otro número: ').grid(row='1', column='0')
etiqueta_resul = Label(ventana, text='Resultado: ').grid(row='2', column='0')
##cuadro de texto
cuadro_ingresar_num = Entry(ventana)
cuadro_ingresar_num.focus()
cuadro_ingresar_num.grid(row='0', column='1')
cuadro_ingresar_num_2 = Entry(ventana)
cuadro_ingresar_num_2.grid(row='1', column='1')
cuadro_resultado = Entry(ventana)
cuadro_resultado.grid(row='2', column='1')
cuadro_promedio= Entry(ventana)
cuadro_promedio.grid(row='5', column='1')

##botones
boton_aceptar = Button(ventana, text='Sumar', bg='green', command=suma).grid(row='4', column='0')
boton_cancelar = Button(ventana, text='Cancelar', bg='red', command=eliminar).grid(row='4', column='1')
boton_promedio = Button(ventana, text='promedio', bg='purple', command=promedio).grid(row='5', column='0')
boton_suma = Button(ventana, text='+', bg='orange', command= lambda:insert_signo('+')).grid(row='5', column='2')

##recoger datos
    

ventana.mainloop()
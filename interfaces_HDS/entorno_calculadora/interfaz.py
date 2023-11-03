from tkinter import *
from operadores import *
ventana = Tk()
#funciones de botones 0-9 tambien operadores
def insertar_dato_pantalla(texto):
    i = len(pantalla.get())
    pantalla.insert(i, texto)

#instanciamos nuestro objeto operadores
ope = operador()

#funcion operacion
def motor_operacion():
    operacion = pantalla.get()

    for i in range(len(operacion)):
        if '+' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.sumar(valor1, valor2)
            pantalla.delete(0, END)
            pantalla.insert(0, resultado)
        elif '-' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.restar(valor1, valor2)
            pantalla.delete(0, END)
            pantalla.insert(0, resultado)
        elif '*' in operacion[i] or 'x' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.multiplicar(valor1, valor2)
            pantalla.delete(0, END)
            pantalla.insert(0, resultado)
        elif '/' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.dividir(valor1, valor2)
            pantalla.delete(0, END)
            pantalla.insert(0, resultado)
#funcion boton borrar
def borrar():
    pantalla.delete(0,END)

ventana.geometry('170x260')
ventana.title('calculadora')
bienvenida = Label(ventana, text='¡Bienvenid@!')
pantalla = Entry(ventana, width=17, bg='#fff00e', font='Bahnschrift')
pantalla.focus()

boton1 = Button(ventana, text='1', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('1'))
boton2 = Button(ventana, text='2', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('2'))
boton3 = Button(ventana, text='3', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('3'))
boton4 = Button(ventana, text='4', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('4'))
boton5 = Button(ventana, text='5', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('5'))
boton6 = Button(ventana, text='6', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('6'))
boton7 = Button(ventana, text='7', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('7'))
boton8 = Button(ventana, text='8', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('8'))
boton9 = Button(ventana, text='9', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('9'))
boton0 = Button(ventana, text='0', bg='#ef0ef0', padx=8, pady=4, command=lambda:insertar_dato_pantalla('0'))

#botones operadores
boton_suma = Button(ventana, text='+', bg='#0f0ef0', padx=8, pady=4,fg='white', command=lambda:insertar_dato_pantalla('+'))
boton_resta = Button(ventana, text='-', bg='#0f0ef0', padx=8, pady=4,fg='white', command=lambda:insertar_dato_pantalla('-'))
boton_multiplicacion = Button(ventana, text='x', bg='#0f0ef0', padx=8,fg='white', pady=4, command=lambda:insertar_dato_pantalla('x'))
boton_division = Button(ventana, text='/', bg='#0f0ef0', padx=8, pady=4,fg='white', command=lambda:insertar_dato_pantalla('/'))
boton_igual = Button(ventana, text='=', bg='#0ee000', padx=28, pady=4, command=motor_operacion)
boton_borrar = Button(ventana, text='Borrar', bg='#f00000', padx=58, pady=4, command=lambda:borrar())

#pocion de la etiqueta saludo y pantalla
bienvenida.grid(row=0, column=0, columnspan=4)
pantalla.grid(row=1, column=0, columnspan=4, padx=6, ipady=4, pady=4)
#pocicion de numeros
boton1.grid(row=3, column=0, pady=4)
boton2.grid(row=3, column=1, pady=4)
boton3.grid(row=3, column=2, pady=4)
boton4.grid(row=4, column=0, pady=4)
boton5.grid(row=4, column=1, pady=4)
boton6.grid(row=4, column=2, pady=4)
boton7.grid(row=5, column=0, pady=4)
boton8.grid(row=5, column=1, pady=4)
boton9.grid(row=5, column=2, pady=4)
boton0.grid(row=6, column=0, pady=4)
#posicion de operadores
boton_suma.grid(row=3, column=3)
boton_resta.grid(row=4, column=3)
boton_multiplicacion.grid(row=5, column=3)
boton_division.grid(row=6, column=3)
boton_igual.grid(row=6, column=1, columnspan=2)
boton_borrar.grid(row=7, column=0, columnspan=4)

ventana.mainloop()
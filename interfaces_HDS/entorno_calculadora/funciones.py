from tkinter import *
from operadores import *
#funciones de botones 0-9 tambien operadores
def insertar_dato_pantalla(objeto, texto):
    i = len(objeto.get())
    objeto.insert(i, texto)

#instanciamos nuestro objeto operadores
ope = operador()

#funcion operacion
def motor_operacion(objeto):
    operacion = objeto.get()

    for i in range(len(operacion)):
        if '+' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.sumar(valor1, valor2)
            objeto.delete(0, END)
            objeto.insert(0, resultado)
        elif '-' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.restar(valor1, valor2)
            objeto.delete(0, END)
            objeto.insert(0, resultado)
        elif '*' in operacion[i] or 'x' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.multiplicar(valor1, valor2)
            objeto.delete(0, END)
            objeto.insert(0, resultado)
        elif '/' in operacion[i]:
            indice = i
            valor1 = int(operacion[:indice])
            valor2 = int(operacion[indice+1:])
            resultado = ope.dividir(valor1, valor2)
            objeto.delete(0, END)
            objeto.insert(0, resultado)

#funcion boton borrar
def borrar(objeto):
    objeto.delete(0,END)
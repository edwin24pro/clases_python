from tkinter import *
def operacion(objeto, signo):
    global num1
    global signo_op
    num1 = objeto.get()
    num1 = float(num1)
    objeto.delete(0, END)
    signo_op=signo

def igual(objeto):
    global num2
    num2 = objeto.get()
    num2 = float(num2)
    objeto.delete(0, END)
    match signo_op:
        case '+':
            objeto.insert(0, num1 + num2)
        case '-':
            objeto.insert(0, num1 - num2)
        case '*':
            objeto.insert(0, num1 * num2)
        case '/':
            objeto.insert(0, num1 / num2)
        case __:objeto.insert(0, 'Error')

def borrar(objeto):
    objeto.delete(0,END)
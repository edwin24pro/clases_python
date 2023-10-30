from tkinter import *
ventana = Tk()
#Creo mis dos widges de orden inferior con al clase Frame()
widget_uno = Frame()
# usar metodo para montar el frame
widget_uno.grid(row = '0', column = '0')
widget_uno.config(width = '100', height = '100')
widget_uno.config(bg='blue')
#El método grid recibe dos parametros el numero de la columna y el numero de la fila donde quiero ubicar widget

ventana.mainloop()
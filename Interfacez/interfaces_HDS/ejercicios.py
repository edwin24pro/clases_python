from tkinter import *
ventana = Tk()
#Creo mis dos widges de orden inferior con al clase Frame()
widget_uno = Frame()
# usar metodo para montar el frame
widget_uno.grid(row = '0', column = '0', padx=5, pady=1, columnspan=2)
widget_uno.config(width = '100', height = '100')
widget_uno.config(bg='black')
#El método grid recibe dos parametros el numero de la columna y el numero de la fila donde quiero ubicar widget

widget_dos = Frame()
# usar metodo para montar el frame
widget_dos.grid(row = '0', column =  '2', padx=5, pady=1, columnspan=2)
widget_dos.config(width = '100', height = '100')
widget_dos.config(bg='blue')

widget_tres = Frame()
# usar metodo para montar el frame
widget_tres.grid(row = '1', columnspan=4)
widget_tres.config(width = '210', height = '100')
widget_tres.config(bg='green')

widget_cuatro = Frame()
# usar metodo para montar el frame
widget_cuatro.grid(row = '2', columnspan=4)
widget_cuatro.config(width = '210', height = '100')
widget_cuatro.config(bg='red')

widget_cinco = Frame()
# usar metodo para montar el frame
widget_cinco.grid(row = '3', column = '0', padx=1, pady=1)
widget_cinco.config(width = '50', height = '50')
widget_cinco.config(bg='red')

widget_seis = Frame()
# usar metodo para montar el frame
widget_seis.grid(row = '3', column = '1', padx=1, pady=1)
widget_seis.config(width = '50', height = '50')
widget_seis.config(bg='red')

widget_siete = Frame()
# usar metodo para montar el frame
widget_siete.grid(row = '3', column = '2',padx=1, pady=1)
widget_siete.config(width = '50', height = '50')
widget_siete.config(bg='red')

widget_ocho = Frame()
# usar metodo para montar el frame
widget_ocho.grid(row = '3', column = '3', padx=1, pady=1)
widget_ocho.config(width = '50', height = '50')
widget_ocho.config(bg='red')
ventana.mainloop()
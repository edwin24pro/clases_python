from tkinter import*
ventana = Tk()
ventana.geometry('300x200')

widget_uno = Frame(ventana, width='150', height='70', padx='15', pady='15')
widget_uno.grid(row='0', column='0')


widget_dos = Frame(ventana, width='150', height='70', padx='15', pady='15')
widget_dos.grid(row='0', column='1')


widget_tres = Frame(ventana, width='280', height='100', padx='10', pady='10')
widget_tres.grid(row='1', column='0', columnspan='2')
widget_tres.config(bg='blue')

etiqueta_nombre_apellido = Label(widget_uno, text='Nombres y Apellidos: ')
etiqueta_dni = Label(widget_uno, text='DNI: ')
etiqueta_Ncelular = Label(widget_uno, text='N° celular: ')

etiqueta_nombre_apellido.pack()
etiqueta_dni.pack()
etiqueta_Ncelular.pack()

cuadro_nombre = Entry(widget_dos)
cuadro_dni = Entry(widget_dos)
cuadro_celular = Entry(widget_dos)

cuadro_nombre.grid(row='0', column='0', padx=2, pady=2)
cuadro_dni.grid(row='1', column='0', padx=2, pady=2)
cuadro_celular.grid(row='2', column='0', padx=2, pady=2)

ventana.mainloop()
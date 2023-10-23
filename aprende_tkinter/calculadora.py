from tkinter import Tk, Button, Label, Entry
ventana = Tk()
ventana.title('Calculadora new')
ventana.geometry('300x350')
etiqueda_saludo = Label(ventana, text= 'Bienvenido aquí')
etiqueda_saludo.grid(column=0, row=0, padx=2, pady=2)


ventana.mainloop()
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkCheckBox
from tkinter import PhotoImage

ventana = CTk()
ventana.geometry('500x600, 350+20')
ventana.minsize(250,300)
ventana.config(bg= '#010101')
ventana.title('Registrate aquí!')
FotoUno = PhotoImage(file= 'F:/Mis cursos/IV ciclo/Lenguaje de programción/Python/ejercicicio_customtkinter/imagenes/llave.png')
ventana.call('wm', 'iconphoto', ventana._w, FotoUno)
etiqueta = CTkLabel(ventana, text='maravilloso')
etiqueta.grid(column=0, row=1)
imagenDos = PhotoImage(file= 'F:/Mis cursos/IV ciclo/Lenguaje de programción/Python/ejercicicio_customtkinter/imagenes/llave.png')
etiquetaDos = CTkLabel(ventana, image= imagenDos).grid(column=2, row=3, padx=50, pady=50)
ventana.mainloop()
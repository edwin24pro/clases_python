from tkinter import *

ventana = Tk()
def decicion():
    user = str(cuadro_usuario.get())
    password = int(cuadro_password.get())
    if user.upper() == 'OSCAR' and password == 123:
        mensaje = 'Bienvenido al sistema'
    else:
        mensaje = 'No encontrado'
    etiqueta_mostrar_texto.config(text=mensaje)

etiqueta = Label(ventana, text='ingrese tu nombre de usuario').pack()
cuadro_usuario = Entry(ventana)
cuadro_password = Entry(ventana, show='*', bg='yellow')

cuadro_usuario.pack()
cuadro_usuario.focus()
cuadro_password.pack()

boton_enviar = Button(ventana, text='enviar', command=decicion).pack()
etiqueta_mostrar_texto = Label(ventana)
etiqueta_mostrar_texto.pack()

ventana.mainloop()

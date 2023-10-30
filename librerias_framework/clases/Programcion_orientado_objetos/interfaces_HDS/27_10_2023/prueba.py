from tkinter import *
ventana = Tk()
def user_focus_in(event):
    if cuadro_user.get()=='Usuario':
        cuadro_user.delete(0,END)
        cuadro_user.config(fg='black')
def user_focus_out(event):
    if cuadro_user.get() == '':
        cuadro_user.config(fg='silver')
        cuadro_user.insert(0,'Usuario')
    
def email_focus_in(event):
    if cuadro_email.get()=='email':
        cuadro_email.delete(0,END)
        cuadro_email.config(fg='black')
def email_focus_out(event):
    if cuadro_email.get() == '':
        cuadro_email.config(fg='silver')
        cuadro_email.insert(0,'email')

def password_focus_in(event):
    if cuadro_password.get()=='password':
        cuadro_password.delete(0,END)
        cuadro_password.config(fg='black')
def password_focus_out(event):
    if cuadro_password.get() == '':
        cuadro_password.config(fg='silver')
        cuadro_password.insert(0,'password')

def login():
    if cuadro_user.get().upper()=='ED' and cuadro_email.get()=='1@.com' and cuadro_password.get()=='123':
        mensaje.config(text='Iniciando sesión...', fg='blue')
    else:
        mensaje.config(text='error!', fg='red')

cuadro_user = Entry(ventana, fg='silver', bg='#ceeeee')
cuadro_user.insert(0,'Usuario')
cuadro_user.bind('<FocusIn>',user_focus_in)
cuadro_user.bind('<FocusOut>',user_focus_out)

cuadro_email = Entry(ventana, fg='silver', bg='#ceeeee')
cuadro_email.insert(0,'email')
cuadro_email.bind('<FocusIn>', email_focus_in)
cuadro_email.bind('<FocusOut>', email_focus_out)

cuadro_password = Entry(ventana, fg='silver', bg='#ceeeee')
cuadro_password.insert(0,'password')
cuadro_password.bind('<FocusIn>', password_focus_in)
cuadro_password.bind('<FocusOut>', password_focus_out)

boton_login = Button(ventana, text='Iniciar',bg='silver',fg='blue', command=login)
mensaje = Label(ventana, text='iniciar sesión', fg='blue')

cuadro_user.pack()
cuadro_email.pack()
cuadro_password.pack()
boton_login.pack()
mensaje.pack()


ventana.mainloop()
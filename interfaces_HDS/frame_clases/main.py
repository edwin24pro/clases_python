from tkinter import *
ventana = Tk()
ventana.title('ejemplo frame')
ventana.geometry('300x200')
frame1 = Frame(ventana, bg='blue').pack(expand=True, fill=BOTH)
frame2 = Frame(ventana, bg='yellow')
frame2.pack(expand=True, fill=BOTH)
frame2.config(cursor='star')
redbuton = Button(frame1, text='red',fg='red')

redbuton.place(relx=.05, rely=.05, relwidth=.25, relheight=.9)
ventana.mainloop()

from tkinter import*
ventana = Tk()
ventana.geometry('400x300')
##espacios
cabecera = Frame(ventana, bg='red', width='400', height='10').grid(row='0', column='0', columnspan='3')
espacio_izquierdo = Frame(ventana, bg='red', width='10', height='300').grid(row='1',column='0', rowspan='2')
espacio_derecho = Frame(ventana, bg='red', width='10', height='300').grid(row='1', column='3', rowspan='2')

##particiiones
frame1 = Frame(ventana,bg='yellow', width='380', height='150').grid(row='2', column='1', rowspan='2', columnspan='2')
frame2 = Frame(ventana,bg='green', width='380', height='140').grid(row='3', column='1', rowspan='2', columnspan='2')
ventana.mainloop()
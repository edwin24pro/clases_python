from tkinter import *
from tkinter import font
import config as cons
class InterfazCalculadora(Tk):
    def __init__(self):
        super().__init__()
        self.configure_ventana()
        self.contruir_widgets()
    def configure_ventana(self):
        self.title('calculadora avanzada')
        #color
        self.configure(bg=cons.COLOR_FONDO_NEGRO)
        #que no se pueda escalar
        self.attributes('-alpha',0.96)
        ##llamar a la funcion centrar ventana
        w,h=370,570#asignamos dos variables en una sola linea
        cons.centrar_ventana(self,w,h)

    def contruir_widgets(self):
        self.operacion_label = Label(self,text='holais', font=('Arial', 16), fg=cons.COLOR_TEXTO_NEGRO, bg=cons.COLOR_FONDO_NEGRO, justify='right')
        self.operacion_label.grid(row=0, column=3, padx=10, pady=10)
        #caja de texto donde se muestra los numeros ingresado
        self.caja_operaciones = Entry(self,width=12, font=('Arial', 40), bd=0, fg=cons.COLOR_TEXTO_NEGRO, bg=cons.COLOR_FONDO_NEGRO, justify='right')
        self.caja_operaciones.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        #creando botones
        botones = [
            'c','%','<','/'
            '7','8','9','*'
            '4','5','6','+'
            '1','2','3','-'
        ]
        row_init = 2
        col_init = 0
        robot_font = font.Font(family='Roboto',size=16)
        for i in botones:
            if i in ['=','*','/','-','+','c','<','%']:
                color_fondo = cons.COLOR_BOTONES_ESPECIAL_NEGRO
                color_font = font.Font(size=16,weight='bold')
            else:
                color_fondo = cons.COLOR_BOTONES_NEGRO
                boton_font = robot_font
            if i=='=':
                Button(self, text=i, width=11,height=2, bg=color_fondo,fg=cons.COLOR_TEXTO_NEGRO,
                relief=FLAT).grid()
            

            if col_init > 3:
                col_init = 0
                row_init +=1
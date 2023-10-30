## clase
class Auto:
    marca = ''
    modelo = 0
    placa = ''

taxi = Auto()

print(taxi.modelo)
print(Auto.modelo)

class Jugadores:
    j1 = 'Messi'
    j2 = 'Cristiano'
    j3 = 'Ronaldiño'

##Ejercicio serio
class nombre:
    pass

victor = nombre()
maria = nombre()

victor.edad = 30
victor.sexo = 'm'
victor.pais = 'peru'

maria.edad = 24
maria.sexo = 'f'
maria.pais = 'chile'

print(victor.edad)
print(maria.edad)
#Metodos
#Es cuando una funcion esta en una clase (método)
## self hace referencia a un determinado objeto
class Matematica:
    def suma(self):
        self.n1 = 1
        self.n2 = 2

s = Matematica()
s.suma()
print(s.n1 + s.n2)
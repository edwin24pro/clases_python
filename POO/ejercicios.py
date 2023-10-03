##1.Haciendo uso de la POO crear un objeto para la entidad celular
class Celular:

    marca = 'huawei'
    boton3 = 'baja volumen'
    pantalla = 'visualizas'

    def boton1(self, estado):
        power = f'El celular esta {estado}'
        return power

dispositivo = Celular()
print(dispositivo.boton1('Activado'))


##2.Haciendo uso de la POO crear un objeto para la entidad vehiculo
class Vehiculo:

    marca = 'volvage'
    motor = 'corean'
    color = 'rojo'

    def llanta(self, estado):
        power = f'La llanta esta {estado}'
        return power

dispositivo = Vehiculo()
print(dispositivo.llanta('Buena'))

##3.Haciendo uso de la POO crear un objeto para la entidad avion
class Avion:

    marca = 'airubus'
    motor = 'corean'
    color = 'rojo'

    def llanta(self, estado):
        power = f'La llanta esta {estado}'
        return power

dispositivo = Avion()
print(dispositivo.llanta('Ponchado'))

##4.Haciendo uso de la POO crear un objeto para la entidad dota2
class Dota2:

    personaje = 'Abaddon'
    trotofeo = 'corean'
    color = 'rojo'

    def arma(self, estado):
        power = f'La espada esta {estado}'
        return power

dispositivo =Dota2()
print(dispositivo.arma('Rota'))
#5.Haciendo uso de la POO crear un objeto para PC
class Pc:
    monitor = 'bueno'
    case = 'chatarra'
    mouse = 'en buen estado'
    teclado = 'en buen estado'

    def cpu(self, pregunta):
        pregunta = input('Que cosa realiza un CPU?: ')
        return pregunta
artefacto = Pc()
print(artefacto.cpu(1))
##6.Haciendo uso de la POO crear un objeto para una impresora
class Impresora:
    bandeja = 'grande'
    case = 'chatarra'
    mouse = 'en buen estado'
    teclado = 'en buen estado'

    def bandeja_hojas(self, bandej):
        estado = bandej
        return estado

artefacto2 = Impresora()
print(artefacto2.bandeja_hojas(bandej='a'))

##7.Haciendo uso de la POO crear un objeto para emitir una factura
class Factura:
    producto = 'soda'
    cantidad = 'en buen estado'
    precio = 'tres soles'

    def total_pagar(self, cantidad):
        precio = 3
        total_pagar = cantidad * precio
        return f'por comprar soda total_pagar {total_pagar}'
    

boletos = Factura()
print(f'''
      ---------------------------------------------------------
      |{boletos.precio} {boletos.cantidad}  {boletos.producto}|
      |                                                       |
      |                   {boletos.total_pagar(cantidad=30)}  |
      |                                                       |
      ---------------------------------------------------------
''')
##Haciendo uso de la POO crear un objeto para la entidad celular
class Celular:

    marca = 'huawei'
    boton3 = 'baja volumen'
    pantalla = 'visualizas'

    def boton1(self, estado):
        power = f'El celular esta {estado}'
        return power

dispositivo = Celular()
print(dispositivo.boton1('Activado'))


##Haciendo uso de la POO crear un objeto para la entidad vehiculo
class Vehiculo:

    marca = 'volvage'
    motor = 'corean'
    color = 'rojo'

    def llanta(self, estado):
        power = f'El celular esta {estado}'
        return power

dispositivo = Vehiculo()
print(dispositivo.boton1('Activado'))

##Haciendo uso de la POO crear un objeto para la entidad avion
class Avion:

    marca = 'airubus'
    motor = 'corean'
    color = 'rojo'

    def llanta(self, estado):
        power = f'El celular esta {estado}'
        return power

dispositivo = Avion()
print(dispositivo.boton1('Activado'))

##Haciendo uso de la POO crear un objeto para la entidad dota2
class Dota2:

    personaje = 'Abaddon'
    motor = 'corean'
    color = 'rojo'

    def llanta(self, estado):
        power = f'El celular esta {estado}'
        return power

dispositivo = Avion()
print(dispositivo.boton1('Activado'))
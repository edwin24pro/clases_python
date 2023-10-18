#Realizar una clase de estudiantes
#Crear un sistema para gestion de productos o control de stock


#entidad entitis. -es un base de datos donde voy a trabajar
estudiantes = [{'id':1, 'nombre':'cristian', 'apellido':'poma ramos', 'Dni': '7847563', 'edad':20,
'Fecha_Nacimiento':'02/12/2002', 'Dirección':'saisa'}]
#casos de uso
class estudiante:
    #atributos de instancia
    def __init__(self, nombre, apellido, Dni, edad, fecha_nacimiento, direccion, calle= 'Jr:'):
        self.nombre = nombre
        self.apellido = apellido
        self.Dni = Dni
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.calle = calle
        self.direccion = direccion

    #Creacionn de metodos
    def mostrar_estudiantes(self):
        mensaje = f'''
        tienes {len(estudiante)} estudiantes
        los estudiantes son:
        {estudiante}
        '''
        return mensaje

    def registrar_estudiante(self):
        nuevo_id = len(estudiantes)+1
        estudiante_nuevo = {
            'id':nuevo_id,
            'nombre':self.nombre,
            'apellido':self.apellido,
            'Dni':self.Dni,
            'edad':self.edad,
            'fecha_Nacimiento':self.fecha_nacimiento,
            'calle':'Jr:',
            'direccion':self.direccion}
        registro_estudiante = estudiantes.append(estudiante_nuevo)
        return f'''el siguiente estudiante se registro exitosamente {estudiante_nuevo}
        '''
    
    def mostrar_estudiante(self, id):
        estudiante_buscar = estudiantes[id-1]
        return estudiante_buscar
    
    def eliminar_estudiante(self, id):
        estudiante_eliminar = estudiantes.pop(id-1)
        return f'''el siguiente registro de estudiante fue eliminado {estudiante_eliminar}'''

    def actualizar_producto(self, id, nombre, apellido, Dni, edad, fecha_nacimiento, direccion, calle= 'Jr:'):
        ubicacion = estudiantes[id-1]
        ubicacion['nombre'] = nombre
        ubicacion['apellido'] = apellido
        ubicacion['Dni'] = Dni
        ubicacion['edad'] = edad
        ubicacion['fecha_Nacimiento'] = fecha_nacimiento
        ubicacion['calle'] = calle
        ubicacion['direccion'] = direccion
        return f'elsiguiente registro fue actualizado {ubicacion}'
estudiante1 = estudiante('Orlando', 'Poma Ramos', '7233763', 23, '12/02/2000', 'Otoca')
estudiante1.registrar_estudiante()
#print(estudiante1.mostrar_estudiante(1))
# print(prod.eliminar_producto(1))
print(estudiante1.actualizar_producto(1,'la blanca', 'jorje chavez', '473y832', 2, '3/3/2000', 'saisa'))
print(f'''
-------------------------------
{estudiantes}
-----------------''')

##Crear unan lista con 10 objetos que contengaan los datos de las tiendas comerciales.
##Ejemplo:
## Relaizar los siguientes ejercicios que tenga los siguientes métodos.
# 1.- Crear un método que me filtre las tiendas que tiene cadaa gerente.
# 2.- Crear un metodo que me muestre los negocios que tienen mas de dos categorías.
# 3.- Crear un metodo que me muestre  solo el nombre y ruc de las tiendas.
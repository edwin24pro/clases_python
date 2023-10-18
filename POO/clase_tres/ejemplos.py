#Crear un sistema para gestion de productos o control de stock


#entidad entitis. -es un base de datos donde voy a trabajar
productos = [{'id':1, 'nombre':'aceite', 'descripción':'10', 'cantidad': 'botella x 1 litro', 'stock':20,
'precio':3.20, 'monda':'soles', 'fecha_vencimiento': '12/12/2023'}]
#casos de uso
class Producto:
    #atributos de instancia
    def __init__(self, nombre, descripción, cantidad, stock, precio, fecha_vencimiento, moneda='soles'):
        self.nombre = nombre
        self.descripción = descripción
        self.cantidad = cantidad
        self.stock = stock
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento

    #Creacionn de metodos
    def mostrar_productos(self):
        mensaje = f'''
        tienes {len(productos)} productos
        los productos son:
        {productos}
        '''
        return mensaje

    def registrar_productos(self):
        nuevo_id = len(productos)+1
        producto_nuevo = {
            'id':nuevo_id,
            'nombre':self.nombre,
            'descripcion':self.descripción,
            'cantidad':self.cantidad,
            'stock':self.stock,
            'precio':self.precio,
            'fecha_vencimiento':self.fecha_vencimiento}
        registro_producto = productos.append(producto_nuevo)
        return f'''el siguiente producto se registra exitosamente {producto_nuevo}
        '''
    
    def mostrar_producto(self, id):
        producto_buscar = productos[id-1]
        return producto_buscar
    
    def eliminar_producto(self, id):
        producto_eliminar = productos.pop(id-1)
        return f'''el siguiente producto fue eliminado {producto_eliminar}'''

    def actualizar_producto(self, id, clave, valor):
        ol = valor
        producto_actualizar = list(filter(lambda el:el[clave]==id, productos))[0].update({clave:valor})
        return 'se actualizo'

prod = Producto('aceite', 'monte sol', '1 litro', 4, 2.10, '12/01/2003)')

# print(prod.registrar_productos())
# print(prod.mostrar_producto(2))
# print(prod.eliminar_producto(1))
print(prod.actualizar_producto('10','descripción', 'edwin'))
print(productos)

#Caso de uso
#Historias de uso
#Producto ower
#Baclog
#MVP
#Prototipos de mierda

#averiguar formas normales (normalizacion de base de datos)
#Programción funcional e python
## Crear un objeto laptop con dos atributos clase y 5 atributos de instancia devera tener
#hasta  3 funcionalidades como mínimo
# OJO: Solo utilizar lo que icimos
class Laptop:
    tipo = 'portatil'
    pantalla = '15.6'

    def __init__(self, marca, modelo, peso, color,tamaño):
        self.marca = marca
        self.modelo = modelo
        self.peso = peso
        self.color = color
        self.tamaño = tamaño

    def escribir(self,ubicacion):
        return f'Esta escuchando en {ubicacion}'

    def mirar_video(self, ubicacion):
        return f'Esta escuchando en {ubicacion}'

    def escuchar_musica(self, ubicacion):
        return f'Esta escuchando en {ubicacion}'

aparato = Laptop('hp', '743hf4', 3, 'negro', '15x10')


usuario1 = aparato.escribir('word')

print(usuario1)

#Crear una clase puesto de mercado que tenga un atributo de clase 5 atributos de instancia y
#5 funcionalidades
#Deberan crear 4 instancias de la clase
class Mercado:
    tipo = 'venta de artefactos'

    def __init__(self, artefacto, precio, tamaño, marca, modelo):
        self.artefacto = artefacto
        self.precio = precio
        self.tamaño = tamaño
        self.marca = marca
        self.modelo = modelo


    def venta_linterna(self, cantidad_compra):
        costo_pagar = int(self.precio) * cantidad_compra
        return costo_pagar

    def venta_laptop(self):
        costo_pagar = int(self.precio) * cantidad_compra
        return costo_pagar


    def venta_televisor(self, cantidad_compra):
        costo_pagar = int(self.precio) * cantidad_compra
        return costo_pagar

    def venta_powerBank(self):
        costo_pagar = int(self.precio) * cantidad_compra
        return costo_pagar

    def venta_celular(self):
        costo_pagar = int(self.precio) * cantidad_compra
        return costo_pagar
#Productos
televisor = Mercado('TELEVISOR', '200','100X100', 'samsung','34NJ3')
impresora = Mercado('Impresora', '300', '30x30x10', 'canon', '74748')
laptop = Mercado('laptop', '1000', '10x20', 'DELL', '334dd')
powerbank = Mercado('powerbank', '60', '8x4', 'cafini', '3673e')
celular = Mercado('celular', '100', '5x4', 'nokia', '3263d')
##ventas
print(f'''
producto: {televisor.artefacto}                 precio: {televisor.precio} soles
------------------------------------------------------------------------------------
detalles:
- marka:    {televisor.marca}
- tamaño:   {televisor.tamaño}
- modelo:   {televisor.modelo}
''')

print(f'''
producto: {impresora.artefacto}                 precio: {impresora.precio} soles
------------------------------------------------------------------------------------
detalles:
- marka:    {impresora.marca}
- tamaño:   {impresora.tamaño}
- modelo:   {impresora.modelo}
''')
#Factura al comprar
producto_comprar = input('producto: ')
if producto_comprar == 'celular':

    print(f'''
                            BOLETO DE VENTA
                            
    producto: {celular.artefacto}                 precio: {celular.precio} soles
    ------------------------------------------------------------------------------------
    detalles:
    - marka:    {celular.marca}
    - tamaño:   {celular.tamaño}             descuento: 20 soles
    - modelo:   {celular.modelo}            total a pagar: {int(celular.precio)-20}
    ''')


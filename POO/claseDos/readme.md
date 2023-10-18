## Instanciando objetos
```python
class Celular:
    ## atributos de de tipo clase
    #que son iguales para todos los códigos
    #que se creen
    familia = 'Smart Phone'
    #atributos de instancia
    #son atributois propios del objeto
    #creamos una funcion inicializadora
    def __init__(self, marca, modelo, imei, nrocelular):
        self.marca = marca
        self.modelo = modelo
        self.imei = imei
        self.nrocelular = nrocelular
    
    #funcionalidades
    def llamar(self, destino):
        return f'llamando a {destino}'
    
#Objeto celular jory
llamandoJory = Celular('poco', 'x5', '4376547', '97347278') # Instanciando mi clse - Creando mi
#objeto celular
print(llamandoJory.marca)
print(llamandoJory.familia)
print(llamandoJory.llamar('china'))
#Objeto celular nadine
llamandoNadine = Celular('alcatel', 'basico', '76344', '9366327')

print(llamandoJory.marca)
print(llamandoJory.familia)
print(llamandoJory.llamar('Ollanta'))
```
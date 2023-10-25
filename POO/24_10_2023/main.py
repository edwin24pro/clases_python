## Tarea
#### 1. crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
##### ejemplo:
# ```python
# tiendas=[
#     {
#         "ruc":857496321,
#         "nombre":"el pichilon",
#         "categoria":["bodega"]
#         "horario_atencion":{
#             "dia":7am-12m,
#             "tarde":2pm-8pm
#         }
#         "gerente":"nadine"
#     }
# ]
# ```
#### Observacion: `las categorias sera 4: abarrotes, farmacia, bodega,restaurant`
#### Observacion: `los gerentes solo podran ser los siguientes: edwin,china,crhistian,nadine`

## Realizar los siguientes ejercicios
#### Crear una clase para tiendas que tenga los suiguientes metodos o casos de uso.
# 1. crear un metodo que me filtre las tiendas que tiene cada gerente
# 2. crear un metodo que me muestre los negocios que tienen mas de dos categorias
# 3. crear un metodo que me muestre solo el nombre y ruc de las tiendas
from bd import *
tienda = Negocio()
comercio_nadine = tienda.bodega('263', 'la nueva', 'abarrote', 'nadine', 'bodega', 'farmacia', 'restaurant')
comercio_china = tienda.bodega('63378', 'sales vivo', 'venta de productos farmacos', 'china', 'restaurant', 'abarrote')
# farmacia2 = tienda.bodega('7437', 'cruz roja', 'venta de farmacos')

# bodega = tienda.bodega('377', 'la chamelita', 'venta de comida')

# restaurant = tienda.bodega('747437', 'cielo nuevo', 'venta de los mejores platos')

bd_comercio = [{'gerente':'nadine','negocio':comercio_nadine}, {'gerente':'china','negocio': comercio_china}]

def tienda_gerente(bd_negocios, nombre_gerente):
    respuesta = list(filter(lambda el:el ['gerente'] == nombre_gerente, bd_negocios))
    return respuesta

def tienda_mas_categoria(bd_negocios):
    respuesta = list(filter(lambda el:len(el ['negocio'][0]['comercio']) > 2, bd_negocios))
    return respuesta

#print(tienda_gerente(bd_comercio, 'china'))
print(tienda_mas_categoria(bd_comercio))

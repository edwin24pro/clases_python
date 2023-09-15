## 1. Crear un program que me pida la edad de una persona si la esdad es mayor o igual a 18 que me muesyre un
#  mensaje 'eres mayor de edad' cso contrario que me muestre un mensaje 'eres menor de edad.
nombre_persona = int(input('Ingresa tu edad: '))
if  nombre_persona >= 18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')

## 2. Una tienda comercial desea hacer un descuento del 20%, crear un program que me determine si el cliente se hace
#  acreedor del descuento teniendo en cuenta lo siguiente, si el cliente realiza una compra de igual o mayor a 1000
#  soless mostrar un mensaje que diga 'ganaste el descuento del 20% ahora pagaras <mostrar el total de al compra
#  menos el deescuento ' en caso la compra no supere los 1000 soles entonces mostrar un menszaje que diga 'no aplicas
#  al descuento <mostrar el monto de la compra'
compra_valor = int(input('ingrese el costo de la compra: '))
if compra_valor >= 1000:
    descuento = 20   
    descontar = (20 * 1000)/100
    valor_pagar = compra_valor - descontar

    print(f'Ganaste un descuento del {descuento}%, usted pagará {valor_pagar} soles y el descuento es de {descontar} soles')
else:
    print(f'No aplicas al descuento, solo compraste valor {compra_valor} soles')


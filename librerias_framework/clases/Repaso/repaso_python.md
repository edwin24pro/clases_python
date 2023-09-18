# **Repaso python**
#### - Tipos de datos
#### - Variables
#### - Operadores
#### - Controles de flujo
#### - Funciones

## Tipos de datos:
Existe los tipos datos primitivos como 'a' string cadena de texto. Ejm
### - String
```python
'hola'
'100'
'True'
'0.1'
```
### - Numérico
Existen variantes.
- Entero.
```python
-99999 - 99999
```
- Flotantes.
```python
-9999.9 - 9999.9
```
### - Boleano
```python
True
False
```
## Variables
Los varables es un lugar donde almacenamos un tipo de dato. El tipo de dato es mutante Ejm.
```python
## En mi variable nobre variable tengo los siguientes tipos de datos
variable = Variable, 'str', 23732, True, Operadores_aritméticos
```
``` python
'''
Consejos para crear un variable.
1- asignarle un nombre coherente al dato que queremos guardar.
2.- Utilizar el signo de asignación (=).
3.- Almacenar el dato.
'''
```
## Operadores
Existen los suguientes operadores.
### Operadores aritméticos
#### - Suma
```python
7+8
```
#### - Resta
```python
7-4
```
#### - Multiplicación
```python
7*3
```
#### - División
```python
## Signo entero
7//2
## Signo flotante
7/2
## Presedencia de operadores
## Primero los operadores de mayor opeso
7+6+6+6+6/1
## Concatenador
'123'+5 => ## '1235'
'ho'+'la'=> ## 'hola'
'hola'*2=> ## holahola
```
## Datos estructurados
Existen dos listas y objetos.
### Listas
```python
## Tepermite almacenar distintos tipos de datos en una sola lista, separados por coma
['nombre',10, False, 1,2]
```
### objetos
```python
## Es parecido a la lista en su almacenamiento pero con un orden para almacenar datos en un objeto necesitamos especificar un indicce y un valor clave=>valor, ademas combina ambas estructuras. 
{'nombre':'jory',
'edad':23,
'sexo':M
'amigos':['edwin','jose','origen':{'departamento':'ayacucho','provincia':'Lucanas'}]
amigos = [{},{},
{}]
}
```
## Controles de flujo
Exiten dostipos:
### Decisión
Solo se ejecuta el código si la condición se cumple o es verdadera.
```python
## Primero especificar eL código que se ejecutará si cumplle una condición.
if condicion:
    print('cush')
else: ## si no es verdad
    print('no HAY')
```
Podremos hacer si la condición sea falsa se ejecute otro código en este caso se utiliza eL 'else'.
Vamos a ver alúnos ejemplos de ambos.
```python
if True:
    print('se ejecuta esto')
else:
    print('Esto nos se ejecuta')
```
```python
if False:
    print('No se ejecuta')
else:
    print('Se ejecuta esto')
```
### Ciclos
Existen dos tipos:
Uno de ellos es iterar cuando sabes la cantidad de veces.
Ejm:
```python
## Primero utilizamos la palabra reservada for y luego un contador y en siguiente
## cantidad a repetir.
for contador numero_a_repetir:

```
El otro es iterar cuando no sabes la cantidad de veces. Ejm:
Ejm:
```python
for i in (1, 2, 3):
    print(i)
# 1 = 1
# 2 = 2
# 3 = 3
```
while
## Funciones
Existen dos tipos:
### Propias del lenguajes
que ya bienen creadas e insertadoas en python y estan listas para ser usadas.
estructura de uso de una funcion, para conocer, este tiene un nombre seguido de parentesis
por medio de parentesis podremos pasarle datos para que pueda funcionar. Ejm.
#### Funciones integradas

```pyhton
print('Chanchito feliz')
# chanchito felis
```
```pyhton
input('referencia')
## Es una funcion que se detiene hasta que se introdusca los datos
```

### Funciones creadas
## Para la 🏡: Averiguar funciones de python mas uzadas con sus ejemplos prácticos
Las siguientes funciones de python son más uzadas.
- **Función divmod(a, b)**, Devuelve el cociente y el sobrante de dividir dos números. Ejm.

```python
divmod(4,2)
#El resultado es (2,0)
## Esta función devuelve de la división el resultado de la cociente  y el residuo.
```
6. **Función abs()**, Retorna el valor absoluto de un número. Ejm.

```python
abs(5)
abs(-5)
# en ambos casos el resultado es 5 por que esta función solo muestra un valor positivo
```
- **Función complex(real, imag)**, Retorna el número complejo con el valor real + imag*1j. También convierte una cadena o un número a un número complejo. Ejm.
```python
comlex(2,2)
complex('3+1j')
#En el primer caso el resultadobes (2,2j) y es de número complejo.
```
- **Función pow(base, exp)**, Retorna base elevado a exp. Ejm.

```python
pow(2,1)
pow(5,-2)
##la respues es 2, y 0.04 respectivamente por el numero que tienen como base y exponente.
```
- **List()**, Con esta función se puede crear un listado y aportan un gran nivel de flexibilidad al trabajar con conjuntos de datos. Ejm.
```python
nombres = 'jhonatan', 'edwin', 'jory'
edad = 1, 2,5
list(nombres) # ['jhonatan', 'edwin', 'jory']
list(edad) # [1,2,5]
## En ambos cosos nos devuelve los datos de la variable en una lista
```
- **Type()**, Se trata de una función básica de Python que se utiliza principalmente con objetivos de depuración de código. Ejm.
```python
nombres = ['jhonatan', 'edwin', 'jory']
pais = 'peru'
edad = 5
viven = True
estatura = 1.2, 4.6, 2.3
calzado = 12.3

type(nombre) #list
type(pais) #str
type(edd) #int
type(vive) #bool
type(estatura) #tuple
type(calzado) #float
##Principalmente se encarga de mostrar el tipo de dato que almacena un variable
```
- **Tuple()**, Permiten crear una lista, pero con dos características diferentes (inmutabilidad, pues sus valores no pueden ser modificados, y rapidez, pues su uso acelera el proceso de cálculo). Ejm.
```python
numeros = 2,3,4,5
tuple(numeros) #(2,3,4,5)
los datos son convertidos a duplas.
```
- **Replace()**, Otra función de texto interesante de este lenguaje de programación que permite sustituir caracteres dentro de una cadena. Ejm.
```python
saludo = 'Buen día'
saludo.replace('a','s') #Buen dís
```
- **Str()**, Conocido también como string, es una función que devuelve la representación de cadena de un número (presenta una secuencia inmutable de caracteres Unicode).
```python

```
- **Ord()** Es una función que muestra el valor ASCII de una cadena de un carácter determinado.
```python

```
- **Input()** Es una función que se utiliza para la entrada de datos por parte de un usuario en los programas desarrollados en Python.
```python

```
- **Chr()**, Devuelve la cadena correspondiente a un número entero en relación con el código Unicode (por ejemplo, chr(97) devuelve la cadena “a”.
```python

```

## Funciones numéricas
- **Sum()**, Una función muy interesante que facilita la suma de valores de una lista o tupla en Python (siempre hablando de números como valores).
```python

```
- **Min()**, Con esta función se puede hallar el número más pequeño dentro de una lista, tupla o dos o más argumentos.
```python

```
- **Max()**, La función contraria a Min() que, en lugar del número más pequeño, devuelve el valor más grande o mayor.
```python

```
- **Range()** Función de Python para generar una sucesión de números enteros de forma personalizada.
```python

```
- **Round()** Cuando se trabaja con números matemáticos es importante disponer de una función capaz de realizar redondeos después de la coma, siendo esta la función de Python que se encarga de este proceso.
```python

```
- **Hex()**, Esta función que se incorporó a partir de la versión 3 de Python, convierte un número entero en una cadena hexadecimal con prefijo “0x”.
```python

```
- **Abs()**, Al utilizar esta función sobre un número se obtiene su valor absoluto.
```python

```
- **Id()**, Se trata de una función nativa que muestra un número entero que es único para cada objeto en memoria.
```python

```
- **Bin()**, Convierte un número entero en una cadena binaria incluyendo el prefijo “0b”.
```python

```

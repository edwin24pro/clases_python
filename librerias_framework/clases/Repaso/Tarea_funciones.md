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
   b# en ambos casos el resultado es 5 por que esta función solo muestra un valor positivo
    ```
- **Función complex(real, imag)**, Retorna el número complejo con el valor real + imag*1j. También convierte una cadena o un número a un número complejo. Ejm.
    ```python
    comlex(2,2)
    complex('3+1j')
    #En el primer caso el resultadobes (2,2j) y es de número complejo.

- **Función pow(base, exp)**, Retorna base elevado a exp. Ejm.
    ```python
    pow(2,2) #será 4
    pow(2,-2) #será 0.04
    ##Realiza una potencia.
- **List()**, Con esta función se puede crear un listado y aportan un gran nivel de flexibilidad al trabajar con conjuntos de datos. Ejm.
    ```python
    numeros = 1,2,3
    letras = 'a','b','c'
    list(numeros) #sera [1,2,3]
    list(letras) #será ['a','b','c']
    ```
- **Type()**, Se trata de una función básica de Python que se utiliza principalmente con objetivos de depuración de código. Ejm.
    ```python
    nombre = 'Emerson'
    edad = 2
    nacio = True
    estatura = 1.2

    type(nombre) #será str
    type(edad) #será int
    type(nacio) #será bool
    type(estatura) #será float

    ##Type muestra el tipo de dato almacenado en la variable.
    ```
- **Tuple()**, Permiten crear una lista, pero con dos características diferentes (inmutabilidad, pues sus valores no pueden ser modificados, y rapidez, pues su uso acelera el proceso de cálculo). Ejm.
    ```python
    nombres = 'jhonatan','javier','solis'
    tuple(nombres) #será ('jhonatan','javier','solis')
    ##Crea una dupla inmutable
    ##La coma define la cantidad de secuencias que hay.
    ```
- **Replace()**, Otra función de texto interesante de este lenguaje de programación que permite sustituir caracteres dentro de una cadena. Ejm.
    ```python
    saludo = 'hola'
    saludo.replace('o','u') #será 'hula'
   #Tiene dos parametros en la primera se pone la letra a remplazar y en la segunda se pone la letra nueva.
    ```
- **Str()**, Conocido también como string, es una función que devuelve la representación de cadena de un número (presenta una secuencia inmutable de caracteres Unicode). Ejm.
    ```python
    numeros = 1,2,3
    convinacion_palabras = ed+you+key
    str(numeros) #será '1,2,3'
    str(convinacion_palabras) #será 'edyoukey'
    ##Actualiza cualquier dato de lanvariable a 'str'.
    ```
- **Ord()** Es una función que muestra el valor ASCII de una cadena de un carácter determinado. Ejm.
    ```python
    vocal1 = 'a'
    vocal2 = 'e'
    ord(letra) #será 97
    ord(vocal2) #será 101
    ##Solo recibe un valor de estring como parametro.
    ```
- **Input()** Es una función que se utiliza para la entrada de datos por parte de un usuario en los programas desarrollados en Python. Ejm.
    ```python
    nombre = input('Ingresa tu nombre: )
    ##Permite dar una referencia para su ingreso más preciso de dato.
    ```
- **Chr()**, Devuelve la cadena correspondiente a un número entero en relación con el código Unicode. Ejm.
    ```python
    chr(64) #Será '@'
    ##Permite ingresar un argumento de valor entero.
    ```

## Funciones numéricas
- **Sum()**, Una función muy interesante que facilita la suma de valores de una lista o tupla en Python (siempre hablando de números como valores).
    ```python
    numeros = [1,2,3,4]
    sum(numeros) #será 10
    ##También suma en las duplas.
    ```
- **Min()**, Con esta función se puede hallar el número más pequeño dentro de una lista, tupla o dos o más argumentos.
    ```python
    numeros = [2,1,3,4]
    min(numeros) #será 1
    realiza una comprovación para obtener el dato menor de todos.
    ```
- **Max()**, La función contraria a Min() que, en lugar del número más pequeño, devuelve el valor más grande o mayor.
    ```python
    numeros = [2,1,3,4]
    max(numeros) #será 4
    ##Obtiene el dator mayor de todos.
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
- **Id()**, Se trata de una función nativa que muestra un número entero que es único para cada objeto en memoria.
```python

```
- **Bin()**, Convierte un número entero en una cadena binaria incluyendo el prefijo “0b”.
```python

```

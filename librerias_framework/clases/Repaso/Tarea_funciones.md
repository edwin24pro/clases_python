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
- **Range()** Función de Python para generar una sucesión de números enteros de forma personalizada. Existen tres formas.
   - range(stop)toma un argumento.
   - range(start, stop)toma dos argumentos.
   - range(start, stop, step)toma tres argumentos.
Sus usos.

    ```python
    ##stop
    for i in range(2):
        print(i) #será 0, 1
    ##start, stop
    for i in range(2,4):
        print(i) #Será 2,3
    ##start, stop, step
    for i in range(2,10,3):
        print(i) #será 2, 5, 8
    ```
- **Round()** Cuando se trabaja con números matemáticos es importante disponer de una función capaz de realizar redondeos después de la coma, siendo esta la función de Python que se encarga de este proceso.
  uso round(numero, digito) Ejm.
    ```python
    numero_decimal = 0.945
    round(numero_decimal,2) #será 0.94
    round(numero_decimal,1) #será 0.9
    rund(numero_decimal) #será 1
    ```
- **Hex()**, Esta función que se incorporó a partir de la versión 3 de Python, convierte un número entero en una cadena hexadecimal con prefijo “0x”. Ejm.
  
    ```python
    hex(4) #será 0x4
    hex('hola') #será error
    ```
- **Id()**, Se trata de una función nativa que muestra un número entero que es único para cada objeto en memoria. Ejm.
  
    ```python
    num1 = 3
    num2 = 4
    id(num1) #será un numero similar 499567470960.
    id(num2 #será otro numero similar 499567470992.
    ```
- **Bin()**, Convierte un número entero en una cadena binaria incluyendo el prefijo “0b”. Ejm.
    ```python
    bin(4) #sera 0b100
    bin(-4) #será -0b100
```
## Averiguar sobre entornos virtuales en python
Diferentes aplicaciones pueden entonces usar entornos virtuales diferentes. Para resolver el ejemplo de requerimientos en conflicto citado anteriormente, la aplicación A puede tener su propio entorno virtual con la versión 1.0 instalada mientras que la aplicación B tiene otro entorno virtual con la versión 2.0. Si la aplicación B requiere que actualizar la librería a la versión 3.0, ésto no afectará el entorno virtual de la aplicación A.

### Creando entornos virtuales
El script usado para crear y manejar entornos virtuales espyvenv. pyvenv normalmente instalará la versión mas reciente de Python que tengas disponible; el script también es instalado con un número de versión, con lo que si tienes múltiples versiones de Python en tu sistema puedes seleccionar una versión de Python específica ejecutando python3 o la versión que desees.

Para crear un entorno virtual, decide en que carpeta quieres crearlo y ejecuta el módulo venv como script con la ruta a la carpeta:
```cmd
python -m venv tutorial-env
```

Esto creará el directorio tutorial-env si no existe, y también creará directorios dentro de él que contienen una copia del intérprete de Python y varios archivos de soporte.

Una ruta común para el directorio de un entorno virtual es .venv. Ese nombre mantiene el directorio típicamente escondido en la consola y fuera de vista mientras le da un nombre que explica cuál es el motivo de su existencia. También permite que no haya conflicto con los ficheros de definición de variables de entorno .env que algunas herramientas soportan.

Una vez creado el entorno virtual, podrás activarlo.

En Windows, ejecuta:
```cmd
tutorial-env\Scripts\activate.bat
```


### Manejando paquetes con pip
You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from the Python Package Index. You can browse the Python Package Index by going to it in your web browser.

pip tiene varios subcomandos: «install», «uninstall», «freeze», etc. (Consulte la guía Instalando módulos de Python para obtener la documentación completa de pip).

Se puede instalar la última versión de un paquete especificando el nombre del paquete:
```cmd
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

También se puede instalar una versión específica de un paquete ingresando el nombre del paquete seguido de == y el número de versión:
```cmd
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

Si se ejecuta de nuevo el comando, pip detectará que la versión ya está instalada y no hará nada. Se puede ingresar un número de versión diferente para instalarlo, o se puede ejecutar pip install --upgrade para actualizar el paquete a la última versión:

```cmd
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```
pip -m pip uninstall seguido de uno o varios nombres de paquetes eliminará los paquetes del entorno virtual.

python -m pip show mostrará información de un paquete en particular:

```cmd
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
```

Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
python -m pip list mostrará todos los paquetes instalados en el entorno virtual:

```cmd
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

python -m pip freeze retorna una lista de paquetes instalados, pero el formato de salida es el requerido por python -m pip install. Una convención común es poner esta lista en un archivo requirements.txt:

```cmd
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

El archivo requirements.txt puede ser agregado al controlador de versiones y distribuido como parte de la aplicación. Los usuarios pueden entonces instalar todos los paquetes necesarios con install -r:

```cmd
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
```
 ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
pip has many more options. Consult the Instalando módulos de Python guide for complete documentation for pip. When you’ve written a package and want to make it available on the Python Package Index.
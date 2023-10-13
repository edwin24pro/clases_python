#1.la siguiente funcion debera retornar la suma de sus parametros
def suma(a,b):
  #reemplazar pass por la sintaxis correcta
  return a+b

print(suma(2,2))

#2. la funcion debera retornar 'es menor' o 'es mayor' segun la edad que pase por parametro
def is_greater_than(edad):
    respuesta = ''
  #reemplazar pass por la sintaxis correcta
    
    if edad < 18:
        return('es menor')
    else:
        return('es mayor')
   
print(is_greater_than(11))
#3. la funcion recibe como parametros dos datos el primero arr recibe una array(lista) el segundo num un numero entero positivo,
# la funcion debera retornar un nuevo array con el num insertado en la tercera posicion del array
lista = ['papa','oca','sal']
lista_num = [4,2,8]
  #reemplazar pass por la sintaxis correcta


def new_array(arr, num):
    lista_nueva = arr
    lista_nueva.insert(3, num)
    return lista_nueva

print(new_array(lista, lista_num))

#4. la funcion recibe una array debera retornar la suma de los numero ejm: [4,2,8,10] retornara 24
lista_num = [4,2,8,10]
def suma_array(arr):
    num = 0
    for i in range(len(arr)):
        num1 = arr[i]
        num+= num1
    return num

print(suma_array(lista_num))
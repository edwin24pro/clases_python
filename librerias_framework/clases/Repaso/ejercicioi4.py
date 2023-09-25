##Escriba una funcion que reciba un numero entero positivo y devuelva sufactorial.
num = 2
for i in range(num):
    factorial = num-i
    factorial += factorial
    print(factorial)

#7. Escribir una funcion que reciva como parametros una lista de nuemros y retorne una
#nueva lista con el cuadro de cada numero de la lista ingresada.
lista = [1,2,3,4]
lista_nueva = []
for i in range(len(lista)):
    numero = lista[i]
    resul_potencia = numero**4
    lista_nueva.append(resul_potencia)
print(lista_nueva)

## 8. Escribir un programa que reciba una cadena de caracteres y devuelva
#  un objeto con cada palabra que contiene y su frecuencia.
nombre = 's o l'
objeto = nombre.object(' ')
print(objeto)
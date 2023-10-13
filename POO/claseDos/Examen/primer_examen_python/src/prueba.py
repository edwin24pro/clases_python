lista = ['papa','oca','sal']
lista_num = [4,2,8]

def new_array(arr, num):
    lista_nueva = arr
    lista_nueva.insert(3, num)
    return lista_nueva

print(new_array(lista, lista_num))
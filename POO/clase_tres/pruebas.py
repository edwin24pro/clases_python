'''
libros = [{'id':1 , 'titulo':'Odisea', 'autor':'homero'},{'id':2, 'titulo':'Ollantay', 'autor':'anonimo'}]

class libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo,
        self.autor = autor

    def actualizar_libro(self, id, titulo, autor):
        ubicacion = libros[id-1]
        ubicacion['titulo'] = titulo
        ubicacion['autor'] = autor
        return f'se cambio el libbro de {ubicacion}'

biblioteca = libro('todas las sangres', 'arguedas')
print(biblioteca.actualizar_libro(1, 'jaimito', 'nuevo'))
print(libros)
'''
alumnos = [{'nombre':'sara', 'edad':'3'}, {'nombre':'jhon', 'edad':'2'}, {'nombre':'cris', 'edad':'2'}]
moda = list(filter(lambda mod:mod['edad']=='2', alumnos))[1]['nombre']
print(f'''
la moda es {moda}
''')

cambio = list(map(lambda mod:{'integrante', mod['nombre']}, alumnos))
print(f'''
El cambio es {cambio}
''')

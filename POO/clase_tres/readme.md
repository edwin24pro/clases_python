filter = El método retorna un elemento que sea True de una lista --> recibe dos parametros
# Funciones anónimas o autoejecutadas en python se les conoce como lanbda
### Su estrucctura:
#### lambda a,b:return a+b ## seejecuta solo
#### funcionamiento
```python
alumnos = [{'nombre':'sara', 'edad':'3'}, {'nombre':'jhon', 'edad':'2'}, {'nombre':'cris', 'edad':'2'}]
moda = list(filter(lambda mod:mod['edad']=='2', alumnos))
print(f'''
la moda es {moda}
''')
```
## Map()
Esta funcion modifica los claves y datos de un nobjeto.
### Funcionamineto

##5. Crear una función por cada operador aritmético que revisa dos parametros y retorne el resultado
#de la operación. OJO, crearse una función que nos permita imprimr el resutado. Konse buils

def suma(a,b):
    resultado = a + b
    return resultado

def resta(a,b):
    resultado = a - b
    return resultado
    
def multiplica(a,b):
    resultado = a * b
    return resultado

def divide(a,b):
    resultado = a / b
    return resultado

def nombre(*args):
    nombre = args[0]
    apellido =  args[1]
    
    return nombre, apellido


print(nombre('edwin'))

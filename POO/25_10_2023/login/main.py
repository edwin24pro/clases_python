from bd import * 
#la variable usuarios estaran disponibles en este archivo
# crear un metodo que sabiendo la fecha de nacimiento me  genere la edad actual
# crear clase para usuario, debera tener los siguientes metodos
# actualizar edad del usuario
# verificar si usuario esta registrado o existe en mis registros
# validar usuario y password
#generamos la edad
def calcular_edad(dni, bd_user):
	calcular_edad = list(filter(lambda el : el['dni']==dni, bd_user))
	fecha_nacimiento = int(calcular_edad[0]['fecha_nacimiento'][6:])
	año_actual = 2023
	edad_actual = año_actual - fecha_nacimiento
	return edad_actual

edad_actual = calcular_edad('4', usuarios)

class Usuario:
  '''
  def  actualizar_edad(self, dni, bd_users, clave, valor_nuevo):
    	actualizar_edad = list(filter(lambda el: el['dni']==dni, bd_users))[0].update({clave:valor_nuevo})
    	return 'se actualizo'
    	'''
  def usuario_existe(self, dni, usuario, bd_ users):
    	usuario_existe = list(filter(lambda el : el['dni'] == dni and el['usuario']==usuario, bd_users))
    	return usuario_existe
    	
registro = Usuario()

#print(registro.actualizar_edad('4', usuarios, 'edad', edad_actual))
print(registro.usuario_existe('4', 'jory', usuarios))


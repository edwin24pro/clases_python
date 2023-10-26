from bd import * 
#la variable usuarios estaran disponibles en este archivo
# crear un metodo que sabiendo la fecha de nacimiento me  genere la edad actual
# crear clase para usuario, debera tener los siguientes metodos
# actualizar edad del usuario
# verificar si usuario esta registrado o existe en mis registros
# validar usuario y password
#generamos la edad

class Usuario:
	def __init__(self, bd_users):
		self.bd_users = bd_users

	def calcular_edad(self, dni):
		calcular_edad = list(filter(lambda el : el['dni']==dni, self.bd_users))
		fecha_nacimiento = int(calcular_edad[0]['fecha_nacimiento'][6:])
		año_actual = 2023
		edad_actual = año_actual - fecha_nacimiento
		return edad_actual

	def actualizar_edad(self, dni, bd_users, clave, valor_nuevo):
		actualizar_edad = list(filter(lambda el: el['dni']==dni, bd_users))[0].update({clave:valor_nuevo})
		return 'se actualizo'
    	
	def usuario_existe(self, dni, usuario, bd_users):
		usuario_existe = bool(list(filter(lambda el : el['dni'] == dni and el['usuario']==usuario, bd_users)))
		if usuario_existe == True:
			return f'el usuario {usuario} existe'
		else:
			return f'el usuario {usuario} no existe'
	
	def login_usuario(self, usuario, password):
		usuario_login = list(filter(lambda el:el['usuario'] == usuario and el['password'] == password, self.bd_users))
		decicion = bool(usuario_login)
		if decicion == True:
			return f'''
			bienvenido a su perfil!
			
			aqui esta sus cosas: 😊
			---------------------------------------------------------------------------------------------------------------------
			{usuario_login}
			---------------------------------------------------------------------------------------------------------------------
			'''
		else:
			return 'Su usuario y contraseña son incorrectos'

registro = Usuario(usuarios)
#edad_actual = calcular_edad('4', usuarios)

registro.actualizar_edad('4', usuarios, 'edad', registro.calcular_edad('4'))
#print(registro.usuario_existe('4', 'jory', usuarios))
#print(registro.calcular_edad('4'))
#print(registro.login_usuario('jory','a111'))
print(usuarios)


from bd_tarea import *
class Tiendas_comerciales:

    def bd_gerente(self,bd_negocios,
        nombre_gerente):
        respuesta=list(filter(lambda el:el
        ["gerente"]==nombre_gerente,
        bd_negocios))
        return respuesta
    
    def tienda_mas_categorias(self,bd_negocios):
        respuesta=list(filter(lambda el:len(el
        ["categoria"])>2,bd_negocios))
        return respuesta

    def ruc_nombre(self,bd_negocios):
        respuesta=list(map(lambda el:{
            "nombre_negocio":el["nombre"],
            "ruc_negocio":el["ruc"]
        },bd_negocios))
        return respuesta

    def eliminar_negocio(self,bd_negocios,ruc):
        respuesta=list(filter(lambda el:el ["ruc"]
        !=ruc,bd_negocios))
        return respuesta

    def actualizar_negocio(self, ruc, bd_negocios, nombre_nuevo, categoria, dia, tarde, noche = '', gerente=''):
        negocio_actualizar = list(filter(lambda el:el['ruc']==ruc,bd_negocios))[0].update({'nombre':nombre_nuevo, 'categoria':categoria, 'gerente':gerente, 'horario_atencion':[dia,tarde,noche]})
        
        return 'se actualizo'

    def actualizar_hora_atension(self, ruc, bd_negocios, hora_dia = '',hora_tarde='', hora_noche=''):
        actualizar_hora_atension =list(filter(lambda el:el['ruc'] == ruc, bd_negocios))[0].update({'dia':hora_dia, 'tarde':hora_tarde, 'noche':hora_noche})
        return 'se cambio la hora de atension'
        

    #otro metodo para agregar un nuevo producto
    def agregar_negocio(self, ruc, bd_negocios, nombre_nuevo, categoria1, categoria2, dia, tarde, noche = '',categoria3 = '', gerente=''):
        id = len(negocios)+1
        agregar = {
        'id':id,
        "ruc":ruc,
        "nombre":nombre_nuevo,
        "categoria":[categoria1,categoria2,categoria3],
        "horario_atencion":{
            "dia":dia,
            "tarde":tarde,
            'noche':noche
        },
        "gerente":gerente
        }
        agregar_negocio = negocios.append(agregar)
        return 'a sido agragado'



    #otro metodo para actualizar el horario de atencion


    def mostrar_todo(self, bd_negocios):
        return bd_negocios
    
gerente=Tiendas_comerciales()
# print(gerente.tienda_gerente(negocios,"china"))
# print(gerente.tienda_mas_categorias(negocios))
#print(gerente.ruc_nombre(negocios))
#print(gerente.eliminar_negocio(negocios,1234))
#print(gerente.actualizar_negocio(1234,negocios,'estrella', 'disfraz','2p,-1pm', '3pm-8pm'))#, 'cerveza', 'chamo', '8am-1pm', '3pm-6pm'))
#print(negocios)
print(gerente.agregar_negocio('3624', negocios, 'la negrita', 'carne', 'latas', '6am-7am', '4pm-5pm', categoria3='leche', gerente='chamelita'))
print(gerente.actualizar_hora_atension('3624', negocios, '2am-4am'))
print(gerente.mostrar_todo(negocios))
class Negocio:
    def bodega(self, ruc, nombre, categoria, gerente, comercio1, comercio2, comercio3='', dia = '7am-12m', tarde= '2pm-8pm'):
        datos = [{'ruc': ruc,
        'nombre': nombre,
        'categoria': categoria,
        'gerente': gerente,
        'comercio': [comercio1, comercio2, comercio3],
        'horario_atension': {dia, tarde}}]
        return datos

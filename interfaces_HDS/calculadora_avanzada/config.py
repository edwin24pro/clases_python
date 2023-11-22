#constantes para el tema oscuro
COLOR_FONDO_NEGRO = '#1a1b28'
COLOR_TEXTO_NEGRO = '#FFFFFF'
COLOR_BOTONES_ESPECIAL_NEGRO = '#52C9DC'
COLOR_BOTONES_NEGRO = '#1E2435'
COLOR_CAJA_TEXTO_NEGRO = '#1A1B28'
#constantes para el tema claro
COLOR_FONDO_LIGHT = '#FFFFFF'
COLOR_TEXTO_LIGHT = '#000000'
COLOR_BOTONES_ESPECIAL_LIGHT = '#52C9DC'
COLOR_BOTONES_LIGHT = '#F2F8FC'
COLOR_CAJA_TEXTO_LIGHT = '#FFFFFF'
#FUNCION QUE NOS PERMITE CENTRAR NUESTRA PANTALLA
def centrar_ventana(objeto, ancho_ventana, largo_ventana):
    pantalla_ancho = objeto.winfo_screenwidth()
    pantalla_largo = objeto.winfo_screenheight()
    x = int((pantalla_ancho/2)-(ancho_ventana/2))
    y = int((pantalla_largo/2)-(largo_ventana/2))
    return objeto.geometry(f'{ancho_ventana}x{largo_ventana}+{x}+{y}')
    
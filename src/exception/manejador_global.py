from pydantic import ValidationError
from src.response.api_respuesta import ApiDeRespuesta
from src.exception.errores_personalizados import ExcepcionBase
from src.exception.mensajes_error import MensajesDeError

# Diccionario de traducción para errores comunes de Pydantic
TRADUCCIONES_PYDANTIC = {
    "value_error.email": "El formato del correo electrónico no es válido",
    "string_too_short": "Debe tener al menos {limit_value} caracteres",
    "string_too_long": "No puede superar los {limit_value} caracteres",
    "missing": "Este campo es obligatorio",
    "value_error.missing": "Este campo es obligatorio",
    "type_error.none.not_allowed": "Este campo no puede estar vacío",
}

def registrar_manejadores_error(app):
    @app.errorhandler(ExcepcionBase)
    def manejar_excepcion_base(e):
        return ApiDeRespuesta.error(e.mensaje_enum, e.detalles, errores=e.errores)

    @app.errorhandler(ValidationError)
    def manejar_validacion_pydantic(e):
        errores = {}
        for error in e.errors():
            # Extraer el campo afectado
            campo = error['loc'][-1]
            tipo_error = error['type']
            msg_original = error['msg']
            
            # Intentar traducir el mensaje según el tipo de error
            mensaje_traducido = TRADUCCIONES_PYDANTIC.get(tipo_error)
            
            if mensaje_traducido:
                # Si el mensaje tiene marcadores de posición como {limit_value}
                ctx = error.get('ctx', {})
                try:
                    mensaje_final = mensaje_traducido.format(**ctx)
                except KeyError:
                    mensaje_final = mensaje_traducido
            else:
                # Traducciones manuales para mensajes comunes de Pydantic v2 si no están en el dict
                if "value is not a valid email address" in msg_original:
                    mensaje_final = "El correo electrónico no es válido"
                elif "at least" in msg_original and "characters" in msg_original:
                    limite = msg_original.split("at least ")[1].split(" ")[0]
                    mensaje_final = f"Debe tener al menos {limite} caracteres"
                elif "at most" in msg_original and "characters" in msg_original:
                    limite = msg_original.split("at most ")[1].split(" ")[0]
                    mensaje_final = f"No puede superar los {limite} caracteres"
                elif "Field required" in msg_original:
                    mensaje_final = "Este campo es obligatorio"
                else:
                    mensaje_final = msg_original # Fallback al original si no se reconoce

            errores[campo] = mensaje_final
            
        return ApiDeRespuesta.error(MensajesDeError.DATOS_INVALIDOS, errores=errores)

    @app.errorhandler(404)
    def manejar_404(e):
        return ApiDeRespuesta.error(MensajesDeError.RECURSO_NO_ENCONTRADO)

    @app.errorhandler(500)
    def manejar_500(e):
        return ApiDeRespuesta.error(MensajesDeError.ERROR_INTERNO)
    
    @app.errorhandler(401)
    def manejar_401(e):
        return ApiDeRespuesta.error(MensajesDeError.NO_AUTORIZADO)

    @app.errorhandler(403)
    def manejar_403(e):
        return ApiDeRespuesta.error(MensajesDeError.ACCESO_DENEGADO)

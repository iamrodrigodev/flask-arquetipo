from src.response.api_respuesta import ApiDeRespuesta
from src.exception.mensajes_error import MensajesDeError

class PuntoDeEntradaDeAutenticacion:
    @staticmethod
    def manejar_no_autorizado():
        return ApiDeRespuesta.error(MensajesDeError.NO_AUTORIZADO, codigo=401)

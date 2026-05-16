from src.response.api_respuesta import ApiDeRespuesta
from src.exception.mensajes_error import MensajesDeError

class ManejadorDeAccesoDenegado:
    @staticmethod
    def manejar_acceso_denegado():
        return ApiDeRespuesta.error(MensajesDeError.ACCESO_DENEGADO, codigo=403)

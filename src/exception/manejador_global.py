from pydantic import ValidationError
from flask import current_app
from src.response.api_respuesta import ApiDeRespuesta
from src.exception.errores_personalizados import ExcepcionBase
from src.exception.mensajes_error import MensajesDeError

def registrar_manejadores_error(app):
    @app.errorhandler(ExcepcionBase)
    def manejar_excepcion_base(e):
        current_app.logger.warn(f"Excepción de negocio: {e.mensaje_enum.mensaje} - Detalles: {e.detalles}")
        return ApiDeRespuesta.error(e.mensaje_enum, e.detalles, errores=e.errores)

    @app.errorhandler(ValidationError)
    def manejar_validacion_pydantic(e):
        errores = {error['loc'][-1]: error['msg'] for error in e.errors()}
        current_app.logger.warn(f"Error de validación de datos: {errores}")
        return ApiDeRespuesta.error(MensajesDeError.DATOS_INVALIDOS, errores=errores)

    @app.errorhandler(404)
    def manejar_404(e):
        current_app.logger.info(f"Recurso no encontrado: {e}")
        return ApiDeRespuesta.error(MensajesDeError.RECURSO_NO_ENCONTRADO)

    @app.errorhandler(500)
    def manejar_500(e):
        current_app.logger.error(f"Error interno no controlado: {str(e)}", exc_info=True)
        return ApiDeRespuesta.error(MensajesDeError.ERROR_INTERNO)
    
    @app.errorhandler(401)
    def manejar_401(e):
        current_app.logger.warn(f"Intento de acceso no autorizado: {e}")
        return ApiDeRespuesta.error(MensajesDeError.NO_AUTORIZADO)

    @app.errorhandler(403)
    def manejar_403(e):
        current_app.logger.warn(f"Acceso denegado (Forbidden): {e}")
        return ApiDeRespuesta.error(MensajesDeError.ACCESO_DENEGADO)

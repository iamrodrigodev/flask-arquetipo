from pydantic import ValidationError
from flask import current_app
from src.response.api_respuesta import ApiDeRespuesta
from src.exception.errores_personalizados import ExcepcionBase
from src.exception.mensajes_error import MensajesDeError

def manejar_excepcion_base(e):
    current_app.logger.warning(f"Excepción de negocio: {e.mensaje_enum.mensaje} - Detalles: {e.detalles}")
    return ApiDeRespuesta.error(e.mensaje_enum, e.detalles, errores=e.errores)

def manejar_validacion_pydantic(e):
    errores = {error['loc'][-1]: error['msg'] for error in e.errors()}
    current_app.logger.warning(f"Error de validación de datos: {errores}")
    return ApiDeRespuesta.error(MensajesDeError.DATOS_INVALIDOS, errores=errores)

def manejar_404(e):
    current_app.logger.info(f"Recurso no encontrado: {e}")
    return ApiDeRespuesta.error(MensajesDeError.RECURSO_NO_ENCONTRADO)

def manejar_500(e):
    current_app.logger.error(f"Error interno no controlado: {str(e)}", exc_info=True)
    return ApiDeRespuesta.error(MensajesDeError.ERROR_INTERNO)

def manejar_401(e):
    current_app.logger.warning(f"Intento de acceso no autorizado: {e}")
    return ApiDeRespuesta.error(MensajesDeError.NO_AUTORIZADO)

def manejar_403(e):
    current_app.logger.warning(f"Acceso denegado (Forbidden): {e}")
    return ApiDeRespuesta.error(MensajesDeError.ACCESO_DENEGADO)

def registrar_manejadores_error(app):
    app.register_error_handler(ExcepcionBase, manejar_excepcion_base)
    app.register_error_handler(ValidationError, manejar_validacion_pydantic)
    app.register_error_handler(404, manejar_404)
    app.register_error_handler(500, manejar_500)
    app.register_error_handler(401, manejar_401)
    app.register_error_handler(403, manejar_403)

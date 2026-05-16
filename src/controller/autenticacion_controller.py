from flask import Blueprint, request
from src.controller.dto.autenticacion.peticion.registro_peticion import RegistroPeticion
from src.controller.dto.autenticacion.peticion.login_peticion import LoginPeticion
from src.service.autenticacion.impl.autenticacion_service_impl import AutenticacionServiceImpl
from src.response.api_respuesta import ApiDeRespuesta
from src.response.mensajes_confirmacion import MensajesDeConfirmacion
from src.security.configuracion_seguridad import login_requerido

autenticacion_bp = Blueprint('autenticacion', __name__)
servicio_auth = AutenticacionServiceImpl()

@autenticacion_bp.route('/registrar-cuenta', methods=['POST'])
def registrar_cuenta():
    peticion = RegistroPeticion(**request.get_json())
    return ApiDeRespuesta.creado(MensajesDeConfirmacion.CUENTA_REGISTRADA, servicio_auth.registrar_cuenta(peticion))

@autenticacion_bp.route('/iniciar-sesion', methods=['POST'])
def iniciar_sesion():
    peticion = LoginPeticion(**request.get_json())
    return ApiDeRespuesta.exito(MensajesDeConfirmacion.LOGIN_EXITOSO, servicio_auth.iniciar_sesion(peticion))

@autenticacion_bp.route('/cerrar-sesion', methods=['POST'])
def cerrar_sesion():
    return ApiDeRespuesta.exito(MensajesDeConfirmacion.SESION_CERRADA)

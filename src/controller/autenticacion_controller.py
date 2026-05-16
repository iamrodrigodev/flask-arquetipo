from flask import Blueprint, request
from src.controller.dto.autenticacion.peticion.registro_peticion import RegistroPeticion
from src.controller.dto.autenticacion.peticion.login_peticion import LoginPeticion
from src.controller.dto.autenticacion.respuesta.inicio_sesion_respuesta import InicioSesionRespuesta, RolRespuesta
from src.service.autenticacion_service import AutenticacionService
from src.response.api_respuesta import ApiDeRespuesta
from src.response.mensajes_confirmacion import MensajesDeConfirmacion
from src.security.filtros import login_requerido

auth_bp = Blueprint('auth', __name__)
servicio_auth = AutenticacionService()

@auth_bp.route('/sesion', methods=['GET'])
@login_requerido
def obtener_sesion():
    usuario = request.usuario_actual
    rol_dto = RolRespuesta(id=usuario.rol.id, nombre=usuario.rol.nombre)
    respuesta_dto = InicioSesionRespuesta(
        id=usuario.id,
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        correo=usuario.correo,
        foto_url=usuario.foto_url,
        rol=rol_dto,
        token=""
    )
    return ApiDeRespuesta.exito(MensajesDeConfirmacion.DATOS_OBTENIDOS, respuesta_dto.dict())

@auth_bp.route('/registrar-cuenta', methods=['POST'])
def registrar_cuenta():
    peticion = RegistroPeticion(**request.get_json())
    servicio_auth.registrar_cuenta(peticion)
    return ApiDeRespuesta.creado(MensajesDeConfirmacion.CUENTA_REGISTRADA)

@auth_bp.route('/iniciar-sesion', methods=['POST'])
def iniciar_sesion():
    peticion = LoginPeticion(**request.get_json())
    usuario, token = servicio_auth.iniciar_sesion(peticion)
    
    rol_dto = RolRespuesta(id=usuario.rol.id, nombre=usuario.rol.nombre)
    respuesta_dto = InicioSesionRespuesta(
        id=usuario.id,
        nombre=usuario.nombre,
        apellidos=usuario.apellidos,
        correo=usuario.correo,
        foto_url=usuario.foto_url,
        rol=rol_dto,
        token=token
    )
    
    return ApiDeRespuesta.exito(MensajesDeConfirmacion.LOGIN_EXITOSO, respuesta_dto.dict())

@auth_bp.route('/cerrar-sesion', methods=['POST'])
def cerrar_sesion():
    return ApiDeRespuesta.exito(MensajesDeConfirmacion.SESION_CERRADA)

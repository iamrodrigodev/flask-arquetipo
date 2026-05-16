from flask import Blueprint, request
from src.service.usuario.impl.usuario_service_impl import UsuarioServiceImpl
from src.response.api_respuesta import ApiDeRespuesta
from src.response.mensajes_confirmacion import MensajesDeConfirmacion
from src.security.configuracion_seguridad import login_requerido

usuario_bp = Blueprint('usuario', __name__)
servicio_usuario = UsuarioServiceImpl()

@usuario_bp.route('/perfil', methods=['GET'])
@login_requerido
def obtener_mi_perfil():
    return ApiDeRespuesta.exito(
        MensajesDeConfirmacion.DATOS_OBTENIDOS, 
        servicio_usuario.obtener_perfil(request.usuario_actual)
    )

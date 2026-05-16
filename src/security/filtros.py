from functools import wraps
from flask import request
from src.security.servicio_jwt import ServicioJwt
from src.response.api_respuesta import ApiDeRespuesta
from src.repository.usuario_repository import UsuarioRepository
from src.exception.mensajes_error import MensajesDeError

def login_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        token = None
        
        # Buscar exclusivamente en el header Authorization: Bearer <token>
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]

        if not token:
            return ApiDeRespuesta.error(MensajesDeError.NO_AUTORIZADO, codigo=401)

        usuario_id = ServicioJwt.decodificar_token(token)
        if not usuario_id:
            return ApiDeRespuesta.error(MensajesDeError.CREDENCIALES_INVALIDAS, codigo=401)

        usuario = UsuarioRepository.buscar_por_id(usuario_id)
        if not usuario:
            return ApiDeRespuesta.error(MensajesDeError.USUARIO_NO_ENCONTRADO, codigo=401)

        # Inyectar usuario en la petición para uso en controladores
        request.usuario_actual = usuario
        return f(*args, **kwargs)
    
    return decorador

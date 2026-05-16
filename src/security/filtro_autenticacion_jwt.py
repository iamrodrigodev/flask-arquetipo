from flask import request
from src.security.servicio_jwt import ServicioJwt
from src.repository.usuario_repository import UsuarioRepository

class FiltroDeAutenticacionJwt:
    @staticmethod
    def extraer_usuario_de_peticion():
        token = None
        if 'Authorization' in request.headers:
            cabecera_auth = request.headers['Authorization']
            if cabecera_auth.startswith('Bearer '):
                token = cabecera_auth.split(" ")[1]

        if not token:
            return None

        usuario_id = ServicioJwt.decodificar_token(token)
        if not usuario_id:
            return None

        return UsuarioRepository.buscar_por_id(usuario_id)

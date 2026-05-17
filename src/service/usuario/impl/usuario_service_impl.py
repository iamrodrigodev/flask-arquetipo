from flask import current_app
from src.service.usuario.i_usuario_service import IUsuarioService
from src.mapper.usuario_mapper import UsuarioMapper
from src.exception.errores_personalizados import ExcepcionDeNegocio
from src.exception.mensajes_error import MensajesDeError

class UsuarioServiceImpl(IUsuarioService):
    def __init__(self):
        self.mapper = UsuarioMapper()

    def obtener_perfil(self, usuario):
        if not usuario:
            raise ExcepcionDeNegocio(MensajesDeError.USUARIO_NO_ENCONTRADO)
            
        current_app.logger.info(f"Obteniendo perfil para el usuario: {usuario.correo}")
        return self.mapper.de_usuario_a_perfil_respuesta(usuario)

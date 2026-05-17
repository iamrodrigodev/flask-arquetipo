import bcrypt
from datetime import datetime, timezone
from flask import current_app
from src.repository.usuario_repository import UsuarioRepository
from src.repository.rol_repository import RolRepository
from src.model.usuario.usuario import Usuario
from src.model.usuario.usuario_direccion import UsuarioDireccion
from src.model.usuario.rol import NombreRol
from src.security.servicio_jwt import ServicioJwt
from src.util.tiempo_util import TiempoUtil
from src.constants.validaciones.seguridad_validacion_constantes import SeguridadValidacionConstantes
from src.exception.errores_personalizados import ExcepcionDeNegocio, ExcepcionDeRecursoNoEncontrado
from src.exception.mensajes_error import MensajesDeError
from src.mapper.autenticacion_mapper import AutenticacionMapper
from src.service.autenticacion.i_autenticacion_service import IAutenticacionService

class AutenticacionServiceImpl(IAutenticacionService):
    def __init__(self):
        self.usuario_repo = UsuarioRepository()
        self.rol_repo = RolRepository()
        self.jwt_service = ServicioJwt()
        self.mapper = AutenticacionMapper()

    def registrar_cuenta(self, datos):
        current_app.logger.info(f"Iniciando registro de cuenta para: {datos.correo}")
        if self.usuario_repo.buscar_por_correo(datos.correo):
            current_app.logger.warning(f"Intento de registro con correo duplicado: {datos.correo}")
            raise ExcepcionDeNegocio(MensajesDeError.EMAIL_DUPLICADO)

        rol_usuario = self.rol_repo.buscar_por_nombre(NombreRol.USUARIO.value)
        if not rol_usuario:
            raise ExcepcionDeRecursoNoEncontrado()

        hashed_pw = bcrypt.hashpw(datos.clave.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        nuevo_usuario = Usuario(
            nombre=datos.nombre,
            apellidos=datos.apellidos,
            correo=datos.correo.lower(),
            clave=hashed_pw,
            telefono=datos.telefono,
            rol=rol_usuario
        )

        if datos.direccion or datos.distrito_id:
            direccion = UsuarioDireccion(
                direccion_exacta=datos.direccion,
                referencia=datos.referencia,
                codigo_postal=datos.codigo_postal,
                distrito_id=datos.distrito_id
            )
            nuevo_usuario.direccion = direccion

        self.usuario_repo.guardar(nuevo_usuario)
        current_app.logger.info(f"Cuenta registrada exitosamente: {datos.correo}")
        return None

    def iniciar_sesion(self, datos):
        current_app.logger.info(f"Intento de inicio de sesión: {datos.correo}")
        usuario = self.usuario_repo.buscar_por_correo(datos.correo.lower())
        if not usuario:
            current_app.logger.warning(f"Usuario no encontrado: {datos.correo}")
            raise ExcepcionDeNegocio(MensajesDeError.CREDENCIALES_INVALIDAS)

        ahora = datetime.now(timezone.utc)
        self._validar_bloqueo_login(usuario, ahora)

        if bcrypt.checkpw(datos.clave.encode('utf-8'), usuario.clave.encode('utf-8')):
            token = self.jwt_service.generar_token(usuario.id)
            self._reiniciar_intentos_login(usuario)
            current_app.logger.info(f"Inicio de sesión exitoso: {datos.correo}")
            return self.mapper.de_usuario_a_inicio_sesion_respuesta(usuario, token)
        else:
            current_app.logger.warning(f"Credenciales inválidas para: {datos.correo}")
            self._registrar_intento_fallido_login(usuario, ahora)
            raise ExcepcionDeNegocio(MensajesDeError.CREDENCIALES_INVALIDAS)

    def obtener_sesion(self, usuario):
        return self.mapper.de_usuario_a_inicio_sesion_respuesta(usuario, "")

    def _validar_bloqueo_login(self, usuario, ahora):
        if usuario.fecha_bloqueo_login:
            if TiempoUtil.esta_en_periodo_de_bloqueo(ahora, usuario.fecha_bloqueo_login, SeguridadValidacionConstantes.LOGIN_MINUTOS_BLOQUEO):
                minutos = TiempoUtil.calcular_minutos_restantes(ahora, usuario.fecha_bloqueo_login, SeguridadValidacionConstantes.LOGIN_MINUTOS_BLOQUEO)
                current_app.logger.warning(f"Cuenta bloqueada temporalmente: {usuario.correo}")
                raise ExcepcionDeNegocio(MensajesDeError.CUENTA_BLOQUEADA, detalles=f"Faltan {minutos} minutos")
            else:
                usuario.intentos_fallidos_login = 0
                usuario.fecha_bloqueo_login = None
                self.usuario_repo.guardar(usuario)

    def _registrar_intento_fallido_login(self, usuario, ahora):
        usuario.intentos_fallidos_login = (usuario.intentos_fallidos_login or 0) + 1
        if usuario.intentos_fallidos_login >= SeguridadValidacionConstantes.LOGIN_MAX_INTENTOS:
            usuario.fecha_bloqueo_login = ahora
            current_app.logger.warning(f"Cuenta bloqueada por exceso de intentos: {usuario.correo}")
        self.usuario_repo.guardar(usuario)

    def _reiniciar_intentos_login(self, usuario):
        if usuario.intentos_fallidos_login > 0:
            usuario.intentos_fallidos_login = 0
            usuario.fecha_bloqueo_login = None
            self.usuario_repo.guardar(usuario)

from functools import wraps
from flask import request
from src.security.filtro_autenticacion_jwt import FiltroDeAutenticacionJwt
from src.security.punto_entrada_autenticacion import PuntoDeEntradaDeAutenticacion
from src.security.manejador_acceso_denegado import ManejadorDeAccesoDenegado
from src.model.usuario.rol import NombreRol

def login_requerido(f):
    @wraps(f)
    def decorador(*args, **kwargs):
        usuario = FiltroDeAutenticacionJwt.extraer_usuario_de_peticion()
        if not usuario:
            return PuntoDeEntradaDeAutenticacion.manejar_no_autorizado()
        
        request.usuario_actual = usuario
        return f(*args, **kwargs)
    return decorador

def requiere_rol(rol_nombre):
    def decorador_real(f):
        @wraps(f)
        @login_requerido
        def decorador(*args, **kwargs):
            usuario = request.usuario_actual
            if usuario.rol.nombre != rol_nombre:
                return ManejadorDeAccesoDenegado.manejar_acceso_denegado()
            return f(*args, **kwargs)
        return decorador
    return decorador_real

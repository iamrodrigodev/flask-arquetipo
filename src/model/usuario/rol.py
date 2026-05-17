from enum import Enum
from src.config.base_de_datos import db
from src.constants.validaciones.seguridad_validacion_constantes import SeguridadValidacionConstantes

class NombreRol(Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    USUARIO = "USUARIO"

class Rol(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'autenticacion'}

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(SeguridadValidacionConstantes.NOMBRE_ROL_MAX), nullable=False, unique=True)

    def __repr__(self):
        return f'<Rol {self.nombre}>'

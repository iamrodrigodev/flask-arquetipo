from enum import Enum
from src.config.base_de_datos import db

class NombreRol(Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    USUARIO = "USUARIO"

class Rol(db.Model):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'autenticacion'}

    id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f'<Rol {self.nombre}>'

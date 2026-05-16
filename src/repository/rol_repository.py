from src.model.usuario.rol import Rol
from src.config.base_de_datos import db

class RolRepository:
    @staticmethod
    def buscar_por_nombre(nombre):
        return Rol.query.filter_by(nombre=nombre).first()

    @staticmethod
    def guardar(rol):
        db.session.add(rol)
        db.session.commit()
        return rol

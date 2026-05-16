from flask import current_app
from src.model.usuario.rol import Rol
from src.config.base_de_datos import db

class RolRepository:
    @staticmethod
    def buscar_por_nombre(nombre):
        return Rol.query.filter_by(nombre=nombre).first()

    @staticmethod
    def guardar(rol):
        try:
            db.session.add(rol)
            db.session.commit()
            current_app.logger.debug(f"Rol guardado en DB: {rol.nombre}")
            return rol
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error al guardar rol {rol.nombre}: {str(e)}")
            raise e

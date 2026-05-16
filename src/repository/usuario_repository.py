from flask import current_app
from src.model.usuario.usuario import Usuario
from src.config.base_de_datos import db

class UsuarioRepository:
    @staticmethod
    def buscar_por_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def buscar_por_correo(correo):
        return Usuario.query.filter_by(correo=correo).first()

    @staticmethod
    def guardar(usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
            current_app.logger.debug(f"Usuario guardado/actualizado en DB: {usuario.correo}")
            return usuario
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error al guardar usuario {usuario.correo}: {str(e)}")
            raise e

    @staticmethod
    def eliminar(usuario):
        try:
            db.session.delete(usuario)
            db.session.commit()
            current_app.logger.info(f"Usuario eliminado de DB: {usuario.correo}")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error al eliminar usuario {usuario.correo}: {str(e)}")
            raise e

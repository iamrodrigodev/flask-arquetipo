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
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def eliminar(usuario):
        db.session.delete(usuario)
        db.session.commit()

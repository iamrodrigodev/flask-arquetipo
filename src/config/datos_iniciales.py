import bcrypt
from src.config.base_de_datos import db
from src.model.usuario.rol import Rol, NombreRol
from src.model.usuario.usuario import Usuario

def sembrar_datos_iniciales(app):
    with app.app_context():
        roles_necesarios = [NombreRol.ADMINISTRADOR.value, NombreRol.USUARIO.value]
        for nombre_rol in roles_necesarios:
            rol_existente = Rol.query.filter_by(nombre=nombre_rol).first()
            if not rol_existente:
                nuevo_rol = Rol(nombre=nombre_rol)
                db.session.add(nuevo_rol)
                db.session.flush()
        
        db.session.commit()

        admin_correo = "admin@arquetipo.com"
        if not Usuario.query.filter_by(correo=admin_correo).first():
            rol_admin = Rol.query.filter_by(nombre=NombreRol.ADMINISTRADOR.value).first()
            pw_hash = bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            admin = Usuario(
                nombre="Administrador",
                apellidos="Arquetipo",
                correo=admin_correo,
                clave=pw_hash,
                rol=rol_admin,
                estado=1
            )
            db.session.add(admin)

        usuario_correo = "usuario@arquetipo.com"
        if not Usuario.query.filter_by(correo=usuario_correo).first():
            rol_user = Rol.query.filter_by(nombre=NombreRol.USUARIO.value).first()
            pw_hash = bcrypt.hashpw("usuario123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            usuario = Usuario(
                nombre="Usuario",
                apellidos="Prueba",
                correo=usuario_correo,
                clave=pw_hash,
                rol=rol_user,
                estado=1
            )
            db.session.add(usuario)

        db.session.commit()
        app.logger.info("Verificación de datos iniciales completada (Roles y Usuarios genéricos asegurados)")

import os
import bcrypt
from sqlalchemy import text
from src.config.base_de_datos import db
from src.model.usuario.rol import Rol, NombreRol
from src.model.usuario.usuario import Usuario
from src.model.ubicacion.departamento import Departamento
from src.model.ubicacion.provincia import Provincia
from src.model.ubicacion.distrito import Distrito

def _asegurar_esquemas(app):
    try:
        db.session.execute(text("CREATE SCHEMA IF NOT EXISTS autenticacion;"))
        db.session.execute(text("CREATE SCHEMA IF NOT EXISTS ubicacion;"))
        db.session.commit()
        app.logger.info("Esquemas verificados")
    except Exception as e:
        app.logger.error(f"Error al crear esquemas: {str(e)}")

def _cargar_catalogos_sql(app):
    if not Departamento.query.first() or not Provincia.query.first() or not Distrito.query.first():
        try:
            sql_path = os.path.join(app.root_path, 'src', 'config', 'sql', 'ubicacion_peru.sql')
            if os.path.exists(sql_path):
                with open(sql_path, 'r', encoding='utf-8') as f:
                    sql_content = f.read()
                    db.session.execute(text(sql_content))
                    db.session.commit()
                    app.logger.info("Catálogo de ubicación (SQL) cargado exitosamente")
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error al cargar catálogo SQL: {str(e)}")

def _sembrar_usuarios_base(app):
    # Asegurar Roles
    roles_necesarios = [NombreRol.ADMINISTRADOR.value, NombreRol.USUARIO.value]
    for nombre_rol in roles_necesarios:
        if not Rol.query.filter_by(nombre=nombre_rol).first():
            db.session.add(Rol(nombre=nombre_rol))
    db.session.commit()

    # Asegurar Admin
    admin_correo = "admin@arquetipo.com"
    if not Usuario.query.filter_by(correo=admin_correo).first():
        rol_admin = Rol.query.filter_by(nombre=NombreRol.ADMINISTRADOR.value).first()
        pw_hash = bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        db.session.add(Usuario(
            nombre="Administrador", apellidos="Arquetipo",
            correo=admin_correo, clave=pw_hash, rol=rol_admin
        ))

    # Asegurar Usuario Prueba
    user_correo = "usuario@arquetipo.com"
    if not Usuario.query.filter_by(correo=user_correo).first():
        rol_user = Rol.query.filter_by(nombre=NombreRol.USUARIO.value).first()
        pw_hash = bcrypt.hashpw("usuario123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        db.session.add(Usuario(
            nombre="Usuario", apellidos="Prueba",
            correo=user_correo, clave=pw_hash, rol=rol_user
        ))
    
    db.session.commit()
    app.logger.info("Semilla de usuarios y roles completada")

def inicializar_datos(app):
    with app.app_context():
        _asegurar_esquemas(app)
        db.create_all()
        _cargar_catalogos_sql(app)
        _sembrar_usuarios_base(app)

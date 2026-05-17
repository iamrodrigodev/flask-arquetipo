from datetime import datetime, timezone
from src.config.base_de_datos import db
from src.constants.validaciones.usuario_validacion_constantes import UsuarioValidacionConstantes

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {'schema': 'autenticacion'}

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(UsuarioValidacionConstantes.NOMBRE_MAX), nullable=False)
    apellidos = db.Column(db.String(UsuarioValidacionConstantes.APELLIDOS_MAX), nullable=False)
    correo = db.Column(db.String(UsuarioValidacionConstantes.CORREO_MAX), nullable=False, unique=True)
    clave = db.Column(db.String(UsuarioValidacionConstantes.CLAVE_MAX), nullable=False)
    telefono = db.Column(db.String(UsuarioValidacionConstantes.TELEFONO_MAX))
    foto_url = db.Column(db.String(UsuarioValidacionConstantes.FOTO_URL_MAX))
    
    estado = db.Column(db.SmallInteger, default=1)
    intentos_fallidos_login = db.Column(db.SmallInteger, default=0)
    fecha_bloqueo_login = db.Column(db.DateTime)
    
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    fecha_actualizacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    rol_id = db.Column(db.SmallInteger, db.ForeignKey('autenticacion.roles.id'), nullable=False)
    rol = db.relationship('Rol', backref=db.backref('usuarios', lazy='dynamic'))

    direccion = db.relationship('UsuarioDireccion', back_populates='usuario', uselist=False, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Usuario {self.correo}>'

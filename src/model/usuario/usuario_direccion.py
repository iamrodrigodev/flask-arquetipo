from datetime import datetime, timezone
from src.config.base_de_datos import db
from src.constants.validaciones.usuario_validacion_constantes import UsuarioValidacionConstantes
from src.constants.validaciones.ubicacion_validacion_constantes import UbicacionValidacionConstantes

class UsuarioDireccion(db.Model):
    __tablename__ = 'usuario_direcciones'
    __table_args__ = {'schema': 'autenticacion'}

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('autenticacion.usuarios.id'), nullable=False, unique=True)
    distrito_id = db.Column(db.String(UbicacionValidacionConstantes.DISTRITO_ID_MAX), db.ForeignKey('ubicacion.ubigeo_peru_distritos.id'))
    
    direccion_exacta = db.Column(db.String(UsuarioValidacionConstantes.DIRECCION_MAX))
    referencia = db.Column(db.String(UsuarioValidacionConstantes.REFERENCIA_MAX))
    codigo_postal = db.Column(db.String(UsuarioValidacionConstantes.CODIGO_POSTAL_MAX))
    
    fecha_creacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    fecha_actualizacion = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    usuario = db.relationship('Usuario', back_populates='direccion')
    distrito = db.relationship('src.model.ubicacion.distrito.Distrito', backref=db.backref('usuario_direcciones', lazy='dynamic'))

    def __repr__(self):
        return f'<UsuarioDireccion {self.usuario_id}>'

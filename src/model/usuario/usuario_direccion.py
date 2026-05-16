from datetime import datetime
from src.config.base_de_datos import db
from src.constants.usuario_constantes import UsuarioValidacionConstantes

class UsuarioDireccion(db.Model):
    __tablename__ = 'usuario_direcciones'
    __table_args__ = {'schema': 'autenticacion'}

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('autenticacion.usuarios.id'), nullable=False, unique=True)
    distrito_id = db.Column(db.String(6))

    direccion_exacta = db.Column(db.String(UsuarioValidacionConstantes.DIRECCION_MAX))
    referencia = db.Column(db.String(UsuarioValidacionConstantes.REFERENCIA_MAX))
    codigo_postal = db.Column(db.String(UsuarioValidacionConstantes.CODIGO_POSTAL_MAX))

    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    usuario = db.relationship('Usuario', back_populates='direccion')

    def __repr__(self):
        return f'<UsuarioDireccion {self.usuario_id}>'

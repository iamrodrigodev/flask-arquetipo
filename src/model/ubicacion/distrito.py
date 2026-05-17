from src.config.base_de_datos import db
from src.constants.validaciones.ubicacion_validacion_constantes import UbicacionValidacionConstantes

class Distrito(db.Model):
    __tablename__ = 'ubigeo_peru_distritos'
    __table_args__ = {'schema': 'ubicacion'}

    id = db.Column(db.String(UbicacionValidacionConstantes.DISTRITO_ID_MAX), primary_key=True)
    nombre = db.Column(db.String(UbicacionValidacionConstantes.NOMBRE_UBICACION_MAX), nullable=False)
    provincia_id = db.Column(db.String(UbicacionValidacionConstantes.PROVINCIA_ID_MAX), db.ForeignKey('ubicacion.ubigeo_peru_provincias.id'), nullable=False)
    
    provincia = db.relationship('Provincia', backref=db.backref('distritos', lazy='dynamic'))

    def __repr__(self):
        return f'<Distrito {self.nombre}>'

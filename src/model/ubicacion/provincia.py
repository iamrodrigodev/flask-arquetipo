from src.config.base_de_datos import db
from src.constants.validaciones.ubicacion_validacion_constantes import UbicacionValidacionConstantes

class Provincia(db.Model):
    __tablename__ = 'ubigeo_peru_provincias'
    __table_args__ = {'schema': 'ubicacion'}

    id = db.Column(db.String(UbicacionValidacionConstantes.PROVINCIA_ID_MAX), primary_key=True)
    nombre = db.Column(db.String(UbicacionValidacionConstantes.NOMBRE_UBICACION_MAX), nullable=False)
    departamento_id = db.Column(db.String(UbicacionValidacionConstantes.DEPARTAMENTO_ID_MAX), db.ForeignKey('ubicacion.ubigeo_peru_departamentos.id'), nullable=False)
    
    departamento = db.relationship('Departamento', backref=db.backref('provincias', lazy='dynamic'))

    def __repr__(self):
        return f'<Provincia {self.nombre}>'

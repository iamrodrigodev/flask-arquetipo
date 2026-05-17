from src.config.base_de_datos import db
from src.constants.validaciones.ubicacion_validacion_constantes import UbicacionValidacionConstantes

class Departamento(db.Model):
    __tablename__ = 'ubigeo_peru_departamentos'
    __table_args__ = {'schema': 'ubicacion'}

    id = db.Column(db.String(UbicacionValidacionConstantes.DEPARTAMENTO_ID_MAX), primary_key=True)
    nombre = db.Column(db.String(UbicacionValidacionConstantes.NOMBRE_UBICACION_MAX), nullable=False)

    def __repr__(self):
        return f'<Departamento {self.nombre}>'

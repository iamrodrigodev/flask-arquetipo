from flask import Blueprint
from src.response.api_respuesta import ApiDeRespuesta
from src.response.mensajes_confirmacion import MensajesDeConfirmacion
from src.mapper.salud_mapper import SaludMapper
from src.constants.sistema_constantes import SistemaConstantes

salud_bp = Blueprint('salud', __name__)

@salud_bp.route('', methods=['GET'])
def verificar_salud():
    datos_salud = SaludMapper.de_estado_a_salud_respuesta(
        servicio=SistemaConstantes.NOMBRE_SERVICIO,
        version=SistemaConstantes.VERSION,
        estado=SistemaConstantes.ESTADO_ACTIVO
    )
    
    return ApiDeRespuesta.exito(
        MensajesDeConfirmacion.DATOS_OBTENIDOS,
        datos_salud
    )

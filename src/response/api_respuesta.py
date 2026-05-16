from flask import jsonify, request
from datetime import datetime

class ApiDeRespuesta:
    @staticmethod
    def exito(mensaje_enum, datos=None, codigo=200):
        mensaje = mensaje_enum.value if hasattr(mensaje_enum, 'value') else mensaje_enum

        respuesta = {
            "estado": codigo,
            "mensaje": mensaje,
            "datos": datos
        }

        return jsonify({k: v for k, v in respuesta.items() if v is not None}), codigo

    @staticmethod
    def error(mensaje_enum, detalles=None, codigo=None, errores=None):
        ahora = datetime.now()

        if hasattr(mensaje_enum, 'mensaje'):
            mensaje = mensaje_enum.mensaje
            codigo_final = codigo or mensaje_enum.codigo
        else:
            mensaje = str(mensaje_enum)
            codigo_final = codigo or 400

        respuesta = {
            "estado": codigo_final,
            "mensaje": mensaje,
            "ruta": request.path,
            "fecha": ahora.strftime("%Y-%m-%d"),
            "hora": ahora.strftime("%H:%M:%S"),
            "errores": errores
        }

        return jsonify({k: v for k, v in respuesta.items() if v is not None}), codigo_final

    @staticmethod
    def creado(mensaje_enum, datos=None):
        return ApiDeRespuesta.exito(mensaje_enum, datos, 201)

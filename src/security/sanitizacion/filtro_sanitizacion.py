from flask import request
from src.security.sanitizacion.sanitizador_entrada import SanitizadorDeEntrada

class FiltroDeSanitizacion:
    _NOMBRES_SENSIBLES = {
        "password", "clave", "claveactual", "nuevaclave", "token",
        "authorization", "jwt", "codigo", "codigoverificacion", "otp", "pin"
    }

    @staticmethod
    def _es_campo_sensible(nombre):
        if not nombre:
            return False
        normalizado = nombre.replace("_", "").replace("-", "").lower()
        return normalizado in FiltroDeSanitizacion._NOMBRES_SENSIBLES

    @staticmethod
    def aplicar_sanitizacion():
        # Sanitizar parámetros de consulta (args)
        if request.args:
            args_sucias = request.args.to_dict()
            args_limpias = {}
            for k, v in args_sucias.items():
                if FiltroDeSanitizacion._es_campo_sensible(k):
                    args_limpias[k] = v
                else:
                    args_limpias[k] = SanitizadorDeEntrada.sanitizar(v)
            # En Flask, request.args es inmutable por defecto, 
            # pero aquí solo definimos la lógica. Para JSON se maneja en DTO.

    @staticmethod
    def sanitizar_diccionario(datos):
        if not isinstance(datos, dict):
            return datos
        
        datos_limpios = {}
        for k, v in datos.items():
            if FiltroDeSanitizacion._es_campo_sensible(k):
                datos_limpios[k] = v
            elif isinstance(v, str):
                datos_limpios[k] = SanitizadorDeEntrada.sanitizar(v)
            elif isinstance(v, dict):
                datos_limpios[k] = FiltroDeSanitizacion.sanitizar_diccionario(v)
            else:
                datos_limpios[k] = v
        return datos_limpios

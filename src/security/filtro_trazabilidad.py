import uuid
from flask import request, g

class FiltroDeTrazabilidad:
    @staticmethod
    def aplicar_trazabilidad():
        g.id_trazabilidad = uuid.uuid4().hex
        g.cliente_ip = FiltroDeTrazabilidad._obtener_ip_cliente()
        g.uri = request.path
        g.metodo = request.method

    @staticmethod
    def _obtener_ip_cliente():
        if request.headers.getlist("X-Forwarded-For"):
            return request.headers.getlist("X-Forwarded-For")[0]
        return request.remote_addr

import logging
from flask import g, has_app_context

class InyectorTrazabilidad(logging.Filter):
    def filter(self, record):
        if has_app_context():
            record.id_trazabilidad = getattr(g, 'id_trazabilidad', 'SISTEMA')
            record.cliente_ip = getattr(g, 'cliente_ip', '0.0.0.0')
        else:
            record.id_trazabilidad = 'SISTEMA'
            record.cliente_ip = '0.0.0.0'
        return True

def configurar_logs(app):
    formato = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(id_trazabilidad)s] [%(cliente_ip)s] [%(name)s]: %(message)s'
    )

    inyector = InyectorTrazabilidad()

    handler_consola = logging.StreamHandler()
    handler_consola.setFormatter(formato)
    handler_consola.addFilter(inyector)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler_consola)

    app.logger.propagate = False

    logging.getLogger('werkzeug').setLevel(logging.ERROR)

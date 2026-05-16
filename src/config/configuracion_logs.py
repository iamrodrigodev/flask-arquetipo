import logging
import os
from logging.handlers import RotatingFileHandler
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
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formato = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(id_trazabilidad)s] [%(cliente_ip)s] [%(name)s]: %(message)s'
    )

    inyector = InyectorTrazabilidad()

    handler_consola = logging.StreamHandler()
    handler_consola.setFormatter(formato)
    handler_consola.addFilter(inyector)

    handler_archivo = RotatingFileHandler(
        os.path.join(log_dir, 'aplicacion.log'),
        maxBytes=10485760,
        backupCount=10
    )
    handler_archivo.setFormatter(formato)
    handler_archivo.addFilter(inyector)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler_consola)
    app.logger.addHandler(handler_archivo)

    app.logger.propagate = False

    logging.getLogger('werkzeug').setLevel(logging.ERROR)

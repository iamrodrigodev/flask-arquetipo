from flask import Flask
from src.config.ajustes import Ajustes
from src.config.base_de_datos import db, migrate
from src.config.configuracion_cors import configurar_cors
from src.config.configuracion_logs import configurar_logs
from src.config.datos_iniciales import inicializar_datos
from src.security.filtro_trazabilidad import FiltroDeTrazabilidad
from src.exception.manejador_global import registrar_manejadores_error
from src.controller.enrutador import registrar_rutas

class IniciadorApp:
    @staticmethod
    def configurar(app: Flask):
        """Encapsula toda la lógica de inicialización y configuración de Flask."""
        # 1. Ajustes y Configuración Base
        app.config.from_object(Ajustes)
        app.secret_key = app.config['CLAVE_SECRETA']
        app.json.sort_keys = False
        
        # 2. Configuración de extensiones y herramientas
        configurar_logs(app)
        configurar_cors(app)
        
        # 3. Middlewares / Filtros
        app.before_request(FiltroDeTrazabilidad.aplicar_trazabilidad)
        
        # 4. Base de Datos
        db.init_app(app)
        migrate.init_app(app, db)
        inicializar_datos(app)
        
        # 5. Blueprints y Manejadores
        registrar_rutas(app)
        registrar_manejadores_error(app)
        
        app.logger.info("Aplicación inicializada")

import os
from flask import Flask
from dotenv import load_dotenv
from src.config.base_de_datos import db, migrate
from src.config.configuracion_cors import configurar_cors
from src.config.configuracion_logs import configurar_logs
from src.security.filtro_trazabilidad import FiltroDeTrazabilidad
from src.exception.manejador_global import registrar_manejadores_error
from src.controller.autenticacion_controller import autenticacion_bp
from src.controller.usuario_controller import usuario_bp

def crear_app():
    load_dotenv()
    
    app = Flask(__name__)
    
    app.config.from_object('src.config.ajustes.Ajustes')
    app.secret_key = app.config['CLAVE_SECRETA']
    
    configurar_logs(app)
    configurar_cors(app)

    app.before_request(FiltroDeTrazabilidad.aplicar_trazabilidad)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(autenticacion_bp, url_prefix='/api/autenticacion')
    app.register_blueprint(usuario_bp, url_prefix='/api/usuario')
    
    registrar_manejadores_error(app)
    
    return app

app = crear_app()

if __name__ == '__main__':
    puerto = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)

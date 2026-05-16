import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from src.config.base_de_datos import db, migrate
from src.exception.manejador_global import registrar_manejadores_error
from src.controller.autenticacion_controller import auth_bp

def crear_app():
    load_dotenv()
    
    app = Flask(__name__)
    
    # Configuración desde objeto (Ajustes en español)
    app.config.from_object('src.config.ajustes.Ajustes')
    
    # Sincronizar SECRET_KEY interno de Flask con CLAVE_SECRETA
    app.secret_key = app.config['CLAVE_SECRETA']
    
    # Extensiones
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registrar Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/autenticacion')
    
    # Manejo de errores global
    registrar_manejadores_error(app)
    
    return app

app = crear_app()

if __name__ == '__main__':
    puerto = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)
